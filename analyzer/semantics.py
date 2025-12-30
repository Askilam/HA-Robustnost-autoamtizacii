# analyzer/semantics.py
from jsonpath_ng.ext import parse
from dataclasses import asdict
import yaml
from typing import List, Dict, Any
from classes.classes import Automation

def apply_rules(automations_ir: List[Automation],errors: List[Dict[str, Any]] = None, rules_path: str = 'analyzer/rules.yaml') -> List[Dict[str, Any]]:
    if errors is None:
        errors = []

    with open(rules_path, 'r', encoding='utf-8') as f:
        rules_data = yaml.safe_load(f)
    rules = rules_data.get('rules', []) if rules_data else []

    for idx, auto in enumerate(automations_ir):
        ir_to_dict = asdict(auto)

        for rule in rules:
            query = rule['query']
            try:
                expr = parse(query)
                matches = expr.find(ir_to_dict)
                values = [match.value for match in matches if match.value is not None]

                condition_met = False
                if rule['condition'] == 'exists' and values:
                    condition_met = True
                elif rule['condition'] == 'empty' and not values:
                    condition_met = True
                elif rule['condition'] == 'equals' and values and all(v == rule.get('value') for v in values):
                    condition_met = True
                elif rule['condition'] == 'contains' and values and any(any(sub in str(v) for sub in rule.get('substring', '').split('|')) for v in values):
                    condition_met = True
                    
                if condition_met:
                    errors.append({
                        'automation_index': idx,
                        'alias': auto.alias or f"Automation #{idx}",
                        'type': 'semantic',
                        'rule': rule['name'],
                        'message': rule['error']
                    })
            except Exception as e:
                errors.append({
                    'automation_index': idx,
                    'alias': auto.alias or f"Automation #{idx}",
                    'type': 'semantic',
                    'rule': rule['name'],
                    'message': f"Unexpected error in rule '{rule['name']}': {e}"
                })
        
