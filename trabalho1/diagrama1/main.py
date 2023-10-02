from Model.Empresa import Empresa
from Model.Nota import Nota
from Model.ItemNota import ItemNota
from Model.Participante import Participante
from Model.Produto import Produto
from datetime import date


if __name__ == '__main__':

    empresa1 = Empresa()
    empresa1.setId(1)
    empresa1.setCodigo(32)
    empresa1.setRazaoSocial("CES/JF")
    empresa1.setEndereco("Rua Halfed, Centro")
    empresa1.setCnpj("25. 101. 1231/0001-15")

    print("Empresa:")
    print(empresa1.__str__())

    nota1 = Nota()
    nota1.setId(510)
    nota1.setData(date(2023, 4, 25))
    nota1.setNumero(5001)

    nota2 = Nota()
    nota2.setId(310)
    nota2.setData(date(2023, 1, 12))
    nota2.setNumero(2001)

    print()
    print("Nota:")
    print(nota1.__str__())

    part1 = Participante()
    part1.set_id(12)
    part1.set_codigo(1415)
    part1.set_razaoSocial("Hamburgueria do Murilo")
    part1.set_cnpj("25. 101. 1231/0001-15")

    print()
    print("Participante:")
    print(part1.__str__())

    item1 = ItemNota()
    item1.setId(91)
    item1.setVrUnitario(100.00)
    item1.setQuantidade(2)

    item2 = ItemNota()
    item2.setId(12)
    item2.setVrUnitario(50.00)
    item2.setQuantidade(4)

    print()
    print("Item:")
    print(item1.__str__())

    produto1 = Produto()
    produto1.setId(41)
    produto1.setCodigo(213)
    produto1.setDescricao("Notebook Gamer Dell")

    print()
    print("Produto:")
    print(produto1.__str__())

    # Associação: Empresa recebe objetos de Nota
    empresa1.addNota(nota1)
    empresa1.addNota(nota2)

    # Associação: Nota recebe objetos de ItensNota
    nota1.addItensNota(item1)
    nota1.addItensNota(item2)

    # Associação: Participante recebe objetos de Nota
    part1.addNota(nota1)
    part1.addNota(nota2)

    # Associação: Produto recebe objetos de ItemNota
    produto1.addNota(item1)
    produto1.addNota(item2)

    print()
    print("Itens em Nota:")
    for item in nota1.getListaItensNota():
        print(f"ID do Item: {item.getId()}")
        print(f"Valor Unitário: R${item.getVrUnitario()}")
        print(f"Quantidade: {item.getQuantidade()}")
        print("------------------------")

    print()
    print("VrTotal:")
    print(f"R$:{nota1.getVrTotal()}")
