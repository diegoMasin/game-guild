import locale

from django.contrib.humanize.templatetags.humanize import intcomma


class Money:
    def __init__(self):
        pass

    def format(self, money):
        try:
            if money:
                locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
                formatted = locale.currency(money, grouping=True, symbol=True)

            else:
                from _decimal import Decimal
                formatted = "R$ " + str(intcomma(round(Decimal(money), 2)))

        # ESTA OCORRENDO ALGUM PROBLEMA COM O LOCALE NO WINDOWS, RESOLVER DEPOIS PARA VOLTAR AO PADRAO QUE É:
        # formatted = '', por enquanto, fica o padrão real brasileiro.
        except:
            from _decimal import Decimal
            formatted = "R$ " + str(intcomma(round(Decimal(money), 2)))

        return formatted


class Cpf:
    def __init__(self):
        """
        Class to interact with CPF numbers
        """
        pass

    def format(self, cpf):
        """
        Method that formats a brazilian CPF
        Tests:
        print Cpf().format('91289037736')
        912.890.377-36
        """
        if cpf:
            formatted = "%s.%s.%s-%s" % (cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11])
        else:
            formatted = ''
        return formatted

    def validate(self, cpf):
        """
        Method to validate a brazilian CPF number
        Based on Pedro Werneck source avaiable at
        www.PythonBrasil.com.br
        Tests:
        print Cpf().validate('91289037736')
        True
        print Cpf().validate('91289037731')
        False
        """
        cpf_invalidos = [11 * str(i) for i in range(10)]
        if cpf in cpf_invalidos:
            return False

        if not cpf.isdigit():
            """ Verifica se o CPF contem pontos e hifens """
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")

        if len(cpf) < 11:
            """ Verifica se o CPF tem 11 digitos """
            return False

        if len(cpf) > 11:
            """ CPF tem que ter 11 digitos """
            return False

        selfcpf = [int(x) for x in cpf]

        cpf = selfcpf[:9]

        while len(cpf) < 11:

            r = sum([(len(cpf) + 1 - i) * v for i, v in [(x, cpf[x]) for x in range(len(cpf))]]) % 11

            if r > 1:
                f = 11 - r
            else:
                f = 0
            cpf.append(f)

        return bool(cpf == selfcpf)


class Cnpj:
    def __init__(self):

        pass

    def format(self, cnpj):

        return "%s.%s.%s/%s-%s" % (cnpj[0:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:14])

    def validate(self, cnpj):

        lista_validacao_um = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        lista_validacao_dois = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        cnpj = cnpj.replace("-", "")
        cnpj = cnpj.replace(".", "")
        cnpj = cnpj.replace("/", "")

        verificadores = cnpj[-2:]

        if len(cnpj) != 14:
            return False

        soma = 0
        id = 0
        for numero in cnpj:

            try:
                lista_validacao_um[id]
            except:
                break

            soma += int(numero) * int(lista_validacao_um[id])
            id += 1

        soma = soma % 11
        if soma < 2:
            digito_um = 0
        else:
            digito_um = 11 - soma

        digito_um = str(digito_um)

        soma = 0
        id = 0

        for numero in cnpj:

            try:
                lista_validacao_dois[id]
            except:
                break

            soma += int(numero) * int(lista_validacao_dois[id])
            id += 1

        soma = soma % 11
        if soma < 2:
            digito_dois = 0
        else:
            digito_dois = 11 - soma

        digito_dois = str(digito_dois)

        return bool(verificadores == digito_um + digito_dois)
