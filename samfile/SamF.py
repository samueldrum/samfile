import re

class SamfReader:
    """This class is just for put your variable into a samf file"""

    def read(self, path):
        # Verificar se o arquivo tem a extensão '.fg'
        if not path.endswith(".samf"):
            raise ValueError("This file is not a 'samf' file")
        
        # Ler o conteúdo do arquivo
        with open(path, "r") as file:
            content = file.read().strip().split("\n")
        
        # Primeira linha é a seção
        the_first = content[0]
        dict_ = {}

        # Verificar e processar a seção
        if re.search(r"<.*>", the_first):
            key = the_first.strip("<>")
            dict_[key] = {}
            
            # Processar cada linha após a seção
            for line in content[1:]:
                if "=" in line:
                    sub_key, sub_value = map(str.strip, line.split("=", 1))
                    
                    # Converter valores numéricos para float
                    if sub_value.isnumeric():
                        sub_value = int(sub_value)
                    if sub_key.isnumeric():
                        sub_key = int(sub_key)

                    # Adicionar ao dicionário
                    dict_[key][sub_key] = sub_value

                else:
                    raise TypeError("You have too put the = symbol attribute")
        
        if re.search(r"<<.*>>", the_first):
            return eval(the_first.strip("<>"))
        
        return dict_

