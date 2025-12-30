# main.py
from pprint import pformat, pprint
from dataclasses import asdict
from loader.yaml_load import load_yaml
from converter_IR.ruamel_to_IR import ruamel_to_IR
from analyzer.semantics import apply_rules 

if __name__ == "__main__":
    raw_data = load_yaml("automatizacia.yaml")
    errors = []

    automations_ir = ruamel_to_IR(raw_data, errors=errors)
    #IR print iba pre mna
    print("\n=== DEBUG: IR automations ===")
    for i, auto in enumerate(automations_ir):
        print(f"\n--- Automation #{i} ---")
        pprint(asdict(auto), width=120)
    

    apply_rules(automations_ir, errors=errors)

    #errors print iba pre mna
    if errors:
        print("Errors found:")
        for err in errors:
            prefix = "[Semantic errors]" if err.get('type') == 'semantic' else "[Syntax error]"
            rule_part = f" ({err.get('rule')})" if 'rule' in err else ""
            alias_part = f" in automation '{err.get('alias', 'unknown')}'" if err.get('alias') else ""
            print(f"- {prefix}{rule_part}: {err['message']}{alias_part}")
    else:
        print("No errors yaaay :)")


    output = {
        'ir': [asdict(auto) for auto in automations_ir],
        'errors': errors
    }
    with open("../BP/parsed_output.txt", "w", encoding="utf-8") as file:
        file.write(pformat(output, indent=2, width=120))
