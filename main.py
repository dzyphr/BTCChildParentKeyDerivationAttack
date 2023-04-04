G_hex = '0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798' #grabbed from https://en.bitcoin.it/wiki/Secp256k1 ***

G = int.from_bytes(bytes.fromhex(G_hex), byteorder='big')
#286650441496909734516720688912544350032790572785058722254415355376215376009112


N_hex = 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141' # ***

N = int.from_bytes(bytes.fromhex(N_hex), byteorder='big')
#115792089237316195423570985008687907852837564279074904382605163141518161494337

#print(G)

#print(N)

L256B = 45785512363230816970838539051071102444734444055822171970071151407697781094851

PPK = 105366245268346348601399826821003822098691517983742654654633135381666943167285

CPrivK1 = (PPK + L256B)  
#print("CPrivK1", CPrivK1)

CPrivK2 = (PPK + L256B) % G
#print("CPrivK2", CPrivK2)

assert(CPrivK1 == CPrivK2) #proof that % G does nothing in this instance

CPrivK = (PPK + L256B) % N #therefore we deduce that N is used for the modulo operation
                            #resulting in expected key 35359668394260970148667380863387016690588397760489922242099123647846562767799
print(CPrivK)

assert(CPrivK == 35359668394260970148667380863387016690588397760489922242099123647846562767799) #checked against expected key

Left256Bits_hex = '6539ae80b3618c22f5f8cc4171d04835570bda8db11b5bf1779afae7ec7c79c3'

L256 = int.from_bytes(bytes.fromhex(Left256Bits_hex), byteorder='big')

print(L256)

PPK_Formula = (CPrivK - L256) % N

PPK_No_modulo = (CPrivK - L256)

print("PPK without doing % N:", PPK_No_modulo)

print(PPK_Formula)

PPK_hex = format(PPK_Formula, 'x')

print(PPK_hex)

assert(PPK_hex == 'e8f32e723decf4051aefac8e2c93c9c5b214313817cdb01a1494b917c8436b35') #proof of Parent PrivKey from Child PrivKey
