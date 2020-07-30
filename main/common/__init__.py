import os
import re
import yaml

def load_config(conf_file):
    with open(conf_file, 'r') as f:
        param_matcher = re.compile(r'.*\$\{([^}^{]+)\}.*')

        def param_constructor(loader, node):
            value = node.value

            params = param_matcher.findall(value)
            for param in params:
                try:
                    param_value = os.environ[param]
                    return value.replace('${' + param + '}', param_value)
                except Exception:
                    pass

            return value

        class VariableLoader(yaml.SafeLoader):
            pass

        VariableLoader.add_implicit_resolver('!param', param_matcher, None)
        VariableLoader.add_constructor('!param', param_constructor)

        config = yaml.load(f.read(), Loader=VariableLoader)

        return config
