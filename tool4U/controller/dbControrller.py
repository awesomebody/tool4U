import cx_Oracle

tns=cx_Oracle.makedsn('rac1',1521,'dave1')

db=cx_Oracle.connect('system','oracle',tns)

print tns

print db.version

vs=db.version.split('.')

print vs

if vs[0]=='10':

   print "This is Oracle 10g!"

db.close()

