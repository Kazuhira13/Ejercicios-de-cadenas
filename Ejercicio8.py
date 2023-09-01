precio = (input("Coloque el precio del producto con dos decimales:"))
precio1 = precio[:precio.find('.')]
deci = precio[precio.find('.')+1:]
print("esta es la cantidad",precio1,"con",deci,"centavos")