# main.py
from pprint import pprint #pre print IR potom vymaz
from dataclasses import asdict #pre print IR potom vymaz
from loader.yaml_load import load_yaml
from converter_IR.ruamel_to_IR import ruamel_to_IR
from analyzer.semantics import apply_rules 

if __name__ == "__main__":
    raw_data = load_yaml("automatizacia.yaml")
    errors = []

    automations_ir = ruamel_to_IR(raw_data, errors=errors)
    #IR print terminal iba pre mna
    #print("\n=== DEBUG: IR automations ===")
    #for i, auto in enumerate(automations_ir):
     #  pprint(asdict(auto), width=120)
    

    apply_rules(automations_ir, errors=errors)
    
    problems = []
    recommendations = []

    for one in errors:
        mess = one.get('message', '').strip()
        if mess.startswith('Recommendation:'):
            recommendations.append(one)
        elif mess.startswith('Semantic error:'):
            problems.append(one)

    output = []
    output.append("Home Assistant automatisation control - Result")
    output.append("===============================================")
    output.append("")
    output.append(f"Automatisations tested: {len(automations_ir)}")
    output.append("")

    if errors:
        if len(problems) > 0: 
            output.append(f"Problems found: {len(problems)}")
            output.append("------------------------\n")
            for i, problem in enumerate(problems, 1):
                alias = problem.get('alias', 'no alias')
                message = problem.get('message')
                output.append(f"{i}.\tAutomatisation:\t{alias}")
                output.append(f"\t{message}")
                output.append("")
        else:
            output.append(f"Problems found: 0")
            output.append("------------------------\n")
        if len(recommendations) > 0: 
            output.append(f"Recommendations found: {len(recommendations)}")
            output.append("------------------------\n")
            for i, problem in enumerate(recommendations, 1):
                alias = problem.get('alias', 'no alias')
                message = problem.get('message')
                output.append(f"{i}.\tAutomatisation:\t{alias}")
                output.append(f"\t{message}")
                output.append("")
        else:
            output.append(f"Recommendations found: 0")
            output.append("------------------------\n")
    else:
        output.append("No problems/recommendations found\n")
        output.append("Result: OK\n")
    #errors print terminal iba pre mna pre testovacie ucely
   # if errors:
    #    print("Errors found:")
     #   for err in errors:
      #      prefix = "[Semantic errors]" if err.get('type') == 'semantic' else "[Syntax error]"
       #     rule_part = f" ({err.get('rule')})" if 'rule' in err else ""
        #    alias_part = f" in automation '{err.get('alias', 'unknown')}'" if err.get('alias') else ""
         #   print(f"- {prefix}{rule_part}: {err['message']}{alias_part}")
    #else:
     #   print("No errors yaaay :)")


    with open("../BP/parsed_output.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(output))
