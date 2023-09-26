from diagrama1.Model.Empresa import Empresa
from diagrama1.Model.Nota import Nota
from diagrama1.Model.ItemNota import ItemNota
from diagrama1.Model.Participante import Participante
from diagrama1.Model.Produto import Produto


if __name__ == '__main__':
    # Criando Empresa
    empresa1 = Empresa()
    empresa1.setIdEmpresa(1)
    empresa1.setCodigo(1001)
    empresa1.setRazaoSocial("Empresa A")
    empresa1.setEndereco("Endereço A")
    empresa1.setCnpj("123456789")

    empresa2 = Empresa()
    empresa2.setIdEmpresa(2)
    empresa2.setCodigo(1002)
    empresa2.setRazaoSocial("Empresa B")
    empresa2.setEndereco("Endereço B")
    empresa2.setCnpj("987654321")

    print()
    print("Empresa:")
    print(f"Id Empresa: {empresa1.getIdEmpresa()}")
    print(f"Código: {empresa1.getCodigo()}")
    print(f"Razão Social: {empresa1.getRazaoSocial()}")
    print(f"Endereço: {empresa1.getEndereco()}")
    print(f"Cnpj: {empresa1.getCnpj()}")

    # Criando Notas
    nota1 = Nota()
    nota1.setEmpresa(empresa1)
    nota1.setIdNota(1)
    nota1.setData("11-09-2023")
    nota1.setNumero(1)

    nota2 = Nota()
    nota2.setEmpresa(empresa2)
    nota2.setIdNota(2)
    nota2.setData("09-06-2023")
    nota2.setNumero(2)

    nota3 = Nota()
    nota2.setEmpresa(empresa2)
    nota3.setIdNota(3)
    nota3.setData("10-01-2021")
    nota3.setNumero(3)

    nota4 = Nota()
    nota4.setEmpresa(empresa1)
    nota4.setIdNota(4)
    nota4.setData("29-03-2024")
    nota4.setNumero(4)
    
    print()
    print("Nota:")
    print(f"Empresa: {nota1.getEmpresa()}")
    print(f"Id Nota : {nota1.getIdNota()}")
    print(f"Data: {nota1.getData()}")
    print(f"Número: {nota1.getNumero()}")

    # Inserido as notas criadas na "lista_notas"
    empresa1.addNota(nota1)
    empresa1.addNota(nota2)
    empresa2.addNota(nota3)
    empresa2.addNota(nota4)

    print()
    print("Lista de notas na empresa 1:")
    for nota in empresa1.getNotas():
        print(nota)

    # Criando ItensNota
    item1 = ItemNota()
    item1.setIdItemNota(3)
    item1.setVrUnitario(10.0)
    item1.setIdItemNota(1)

    item2 = ItemNota()
    item2.setIdItemNota(2)
    item2.setVrUnitario(50.0)
    item2.setIdItemNota(2)

    item3 = ItemNota()
    item3.setIdItemNota(3)
    item3.setVrUnitario(25.0)
    item3.setIdItemNota(4)

    item4 = ItemNota()
    item4.setIdItemNota(4)
    item4.setVrUnitario(12.5)
    item4.setIdItemNota(4)

    # Criando Produtos
    prod1 = Produto()
    prod1.setIdProduto(1)
    prod1.setCodigoProduto("001")
    prod1.setDescricao("Mouse")

    prod2 = Produto()
    prod2.setIdProduto(2)
    prod2.setCodigoProduto("002")
    prod2.setDescricao("Monitor")

    prod3 = Produto()
    prod3.setIdProduto(3)
    prod3.setCodigoProduto("003")
    prod3.setDescricao("Teclado")

    prod4 = Produto()
    prod4.setIdProduto(4)
    prod4.setCodigoProduto("004")
    prod4.setDescricao("TV")

    print()
    print("Produto:")
    print(f"Id Produto: {prod1.getIdProduto()}")
    print(f"Código Produto: {prod1.getCodigoProduto()}")
    print(f"Descrição: {prod1.getDescricao()}")

    partici1 = Participante()
    partici1.setIdParticipante(1)
    partici1.setCodigoParticipante(32)
    partici1.setRazaoSocial("ATACADÃO DO MURILO")
    partici1.setCnpj("XX. XXX. XXX/0001-XX")

    partici2 = Participante()
    partici2.setIdParticipante(2)
    partici2.setCodigoParticipante(23)
    partici2.setRazaoSocial("CARTÓRIO DO GIÁCOPO")
    partici2.setCnpj("XX. XXX. XXX/0001-XX")

    partici3 = Participante()
    partici3.setIdParticipante(3)
    partici3.setCodigoParticipante(21)
    partici3.setRazaoSocial("MURILO's CAKES FACTORY")
    partici3.setCnpj("XX. XXX. XXX/0001-XX")

    print()
    print("Participante:")
    print(f"Id: {partici1.getIdParticipante()}")
    print(f"Código: {partici1.getCodigoParticipante()}")
    print(f"Razão Social: {partici1.getRazaoSocial()}")
    print(f"CNPJ: {partici1.getCnpj()}")

    # Notas pertencentes a empresa1
    nota1.addItensNota(item1)
    nota2.addItensNota(item2)
    # Notas pertencentes a empresa2
    nota3.addItensNota(item3)
    nota4.addItensNota(item4)

    # Adicionando um ‘item’ a lista de produtos
    item1.addProduto(prod1)
    item2.addProduto(prod2)

    # Aqui iremos listar as notas associadas a cada empresa
    notas_empresa1 = empresa1.getNotas()
    notas_empresa2 = empresa2.getNotas()

    print()
    print("Notas da empresa: \n")

    print("Notas da empresa 1: ")
    for nota in notas_empresa1:
        print(
            f"ID: {nota.getIdNota()}, Data: {nota.getData()}, Número: {nota.getNumero()}, VrTotal: R${nota.getVrTotal()}")
    print("\n")

    print("Notas da empresa 2:")
    for nota in notas_empresa2:
        print(
            f"ID: {nota.getIdNota()}, Data: {nota.getData()}, Número: {nota.getNumero()}, VrTotal: R${nota.getVrTotal()}")
