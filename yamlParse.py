# YAML MULTIPLE DOCUMENT PARSER CLASS #

#%%
import ruamel.yaml

class YamlParser:

    def __init__(self, name:str, setDesired:int=1):
        
        assert setDesired > 0, f"Desired set: {setDesired}, must be positive and greater than zero (1st set = 0th index)"

        self.name = name
        self.setDesired = setDesired

        # actions to execute
        YamlParser.parseYaml(self)

    # parse .yaml for desired document
    def parseYaml(self):

        with open(self.name, 'r') as f:
            data = ruamel.yaml.safe_load_all(f)

            iter = 0
            self.docNum = 0
            for doc in data:
                self.docNum += 1
                if iter == self.setDesired-1:
                    self.docDesired = doc
                    break
                iter += 1

        return self.docNum, self.docDesired
