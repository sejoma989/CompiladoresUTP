# -----------------------------------------------------------------------------
# calc.py
# -----------------------------------------------------------------------------

from sly import Parser
from léxico_lola import CalcLexer

class CalcParser(Parser):
	debugfile='parser.out'#control de depuración
	

	tokens = CalcLexer.tokens

	
	'''
	tipoSimple : tipoBasico
		|	ID conjuntoExpresiones
		;
	'''
	
	@_('tipoBasico', 
	'ID conjuntoExpresiones')
	def tipoSimple(self, p):
		pass
		
	'''
	tipoBasico : 'BIT'
		| 'TS'
		| 'OC'
		;
	'''
	@_('BIT', 
	'TS', 
	'OC')
	def tipoBasico(self, p):
		pass
	
	'''
	conjuntoExpresiones : '(' listaExpresiones ')'
	|	
	;
	'''
	

<<<<<<< HEAD
	@_('"(" listaExpresiones ")"', 
	'empty')
=======
	@_('empty', '"(" listaExpresiones ")"')
>>>>>>> 49d3f0bb3a047edb074af39cdb8dd6edcf835b42
	def conjuntoExpresiones(self, p):
		pass
		
	'''
	listaExpresiones : expresion expresionComa
		;
	'''
	
	@_('expresion expresionComa')
	def listaExpresiones(self, p):
		pass
		
	'''
	expresionComa :  expresionComa "," expresion
	|	"," expresion
	|
	;
	'''

<<<<<<< HEAD
	@_('expresionComa "," expresion', 
	'"," expresion', 
	'empty')
=======
	@_('expresionComa', '"," expresion')
>>>>>>> 49d3f0bb3a047edb074af39cdb8dd6edcf835b42
	def expresionComa(self, p):
		pass
		
	'''
	tipo : expresionCorchete tipoSimple
	;
	'''
	@_('expresionCorchete tipoSimple')

	def tipo(self, p):
		pass
		
	'''
	expresionCorchete : expresionCorchete "[" expresion "]"
	| "[" expresion "]"
	|
	;
	'''
	@_('expresionCorchete "[" expresion "]"', 
	'"[" expresion "]"',
	'empty')
	def expresionCorchete(self, p):
		pass
		
	'''

	declaracionConstante : ID ":=" expresion ";"'
	;
	'''
	@_('ID DOSPUNTOSIGUAL expresion ";"')
	def declaracionConstante(self, p):
		pass
	
	'''
	declaracionVariable : listaId ":" tipo ";"
	;
	'''
	@_('listaId ":" tipo ";"')
	def declaracionVariable(self, p):
		pass
		
	'''

	listaId : ID IDComa
		;
	'''
	@_('ID IDComa')
	def listaId(self, p):
		pass
		
	'''
	IDComa : IDComa "," ID
	|	"," ID
	|
	;
	'''

<<<<<<< HEAD
	@_('IDComa "," ID', 
	'"," ID',
	'empty')
=======
	@_('IDComa', '"," ID')
>>>>>>> 49d3f0bb3a047edb074af39cdb8dd6edcf835b42
	def IDComa(self, p):
		pass
	
	'''
	selector : selector "." ID
	|	selector "." INTEGER
	|	selector "[" expresion "]"
	|	"." ID
	|	"." INTEGER
	|	"[" expresion "]"
	|
	;
	'''
	@_('selector "." ID', 
	'selector "." INTEGER', 
	'selector "[" expresion "]"', 
	'"." ID',
	'"." INTEGER',
	'"[" expresion "]"',
	'empty')
	def selector(self, p):
		pass
	
	'''
	factor : ID selector
	|	valorLogico
	|	INTEGER
	|	"~" factor
	|	"?" factor
	|	"(" expresion ")"
	|	"MUX" "(" expresion ":" expresion "," expresion ")"
	|	"MUX" "(" expresion "," expresion ":" expresion "," expresion "," expresion "," expresion)
	|	"REG" "(" expresionComa2 expresion ")"
	|	"LATCH" "(" expresion "," expresion ")"
	|	"SR" "(" expresion "," expresion ")"
	;
	'''
	@_('ID selector', 
	'LOGICVALUE', 
	'INTEGER', 
	'"~" factor', 
	'"?" factor', 
	'"(" expresion ")"', 
	'MUX "(" expresion ":" expresion "," expresion ")"', 
	'MUX "(" expresion "," expresion ":" expresion "," expresion "," expresion "," expresion ")"', 
	'REG "(" expresionComa2 expresion', 
	'LATCH "(" expresion "," expresion ")"', 
	'SR "(" expresion , expresion ")"')
	def factor(self, p):
		pass
		
	'''
	expresionComa2 : expresion ","
	|	
	;
	'''
	@_('expresion ","', 'empty')
	def expresionComa2(self, p):
		pass
		
	'''
	termino : factor terminoOperadores
	;
	'''	
	@_('factor terminoOperadores')
	def termino(self, p):
		pass
		
	'''
	terminoOperadores : terminoOperadores simbolosProd factor
	|	simbolosProd factor
	|
	;
	'''
	@_('terminoOperadores simbolosProd factor', 
	'simbolosProd factor',
	'empty')
	def terminoOperadores(self, p):
		pass
	
	'''
	simbolosProd : "*"
	|	"/"
	|	"DIV"
	|	"MOD"
	;
	'''
	@_('"*"',
	'"/"',
	'DIV',
	'MOD')
	def simbolosProd(self, p):
		pass
		
	'''
	expresion : termino terminoMasMenos
	;
	'''
	@_('termino terminoMasMenos')
	def expresion(self, p):
		pass
		
	'''
	terminoMasMenos : terminoMasMenos simbolosMasMenos termino
	|	simbolosMasMenos termino
	|
	;
	'''
	@_('terminoMasMenos simbolosMasMenos termino', 
	'simbolosMasMenos termino',
	'empty')
	def terminoMasMenos(self, p):
		pass
		
	'''
	simbolosMasMenos : "+"
	|	"-"
	;
	'''
	@_('"+"', 
	'"-"')
	def simbolosMasMenos(self, p):
		pass
		
	'''
	asignacion : ID selector ":=" condicionOr expresion
	;
	'''
	@_('ID selector DOSPUNTOSIGUAL condicionOr expresion')
	def asignacion(self, p):
		pass
		
	'''
	condicionOr : condicion "|"
	|	
	;
	'''
	@_('condicion "|"',
	'empty')
	def condicionOr(self, p):
		pass
		
	'''
	condicion : expresion
	;
	'''
	@_('expresion')
	def condicion(self, p):
		pass
		
	'''
	relacion : expresion simbolosRelacion expresion
	;
	'''
	@_('expresion simbolosRelacion expresion')
	def relacion(self, p):
		pass
		
	'''
	simbolosRelacion : "="
	|	"#"
	|	"<"
	|	"<="
	|	">"
	|	">="
	;
	'''
	@_('"="', 
	'"#"', 
	'"<"', 
	'MENORIGUAL', 
	'">"', 
	'MAYORIGUAL')
	def simbolosRelacion(self, p):
		pass
		
	'''
	sentenciaSi : "IF" relacion "THEN" sentenciaSecuencia sentenciaSiSino sentenciaSiEntonces "END"
	;
	'''
	@_('IF relacion THEN sentenciaSecuencia sentenciaSiSino sentenciaSiEntonces END')
	def sentenciaSi(self, p):
		pass
		
	'''
	sentenciaSiSino : sentenciaSiSino "ELSIF" relacion "THEN" sentenciaSecuencia
	|	"ELSIF" relacion "THEN" sentenciaSecuencia
	|
	;
	'''
	@_('sentenciaSiSino ELSIF relacion THEN sentenciaSecuencia',
	'ELSIF relacion THEN sentenciaSecuencia',
	'empty')
	def sentenciaSiSino(self, p):
		pass
		
	'''
	sentenciaSiEntonces : "ELSE" sentenciaSecuencia
	|
	;
	'''
	@_('ELSE sentenciaSecuencia',
	'empty')
	def sentenciaSiEntonces(self, p):
		pass
		
	'''
	sentenciaPara : "FOR" ID ":=" expresion ".." expresion "DO" sentenciaSecuencia "END"
	;
	'''
	@_('FOR ID DOSPUNTOSIGUAL expresion DOBLEPUNTO expresion DO sentenciaSecuencia END')
	def sentenciaPara(self, p):
		pass
		
	'''
	sentencia : asignacion
	|	asignacionUnidad
	|	sentenciaSi
	|	sentenciaPara
	|
	;
	'''
	@_('asignacion', 
	'asignacionUnidad', 
	'sentenciaSi', 
	'sentenciaPara',
	'empty')
	def sentencia(self, p):
		pass
	
	'''
	sentenciaSecuencia : sentencia sentenciaPuntoComa
	;
	'''
	@_('sentencia sentenciaPuntoComa')
	def sentenciaSecuencia(self, p):
		pass
		
	'''
	sentenciaPuntoComa : sentenciaPuntoComa ";" sentencia
	|	";" sentencia
	|
	;
	'''
	@_('sentenciaPuntoComa ";" sentencia', 
	'";" sentencia',
	'empty')
	def sentenciaPuntoComa(self, p):
		pass
		
	'''
	modulo : "MODULE" ID ";" 
	declaracionTipoPuntoComa 
	declaracionConstanteCONST 
	declaracionVariableIN 
	declaracionVariableINOUT 
	declaracionVariableOUT 
	declaracionVariableVAR 
	sentenciaSecuenciaBEGIN 
	END ID "."
	;
	'''
	@_('MODULE ID ";" declaracionTipoPuntoComa declaracionConstanteCONST declaracionVariableIN declaracionVariableINOUT declaracionVariableOUT declaracionVariableVAR sentenciaSecuenciaBEGIN END ID "."')
	def modulo(self, p):
		pass
		
	'''
	declaracionTipoPuntoComa : declaracionTipoPuntoComa declaracionTipo ";"
	|	declaracionTipo ";"
	|
	;
	'''
	@_('declaracionTipoPuntoComa declaracionTipo ";"',
	'declaracionTipo ";"',
	'empty')
	def declaracionTipoPuntoComa(self, p):
		pass
		
	'''
	declaracionConstanteCONST : "CONST" declaracionConstanteRecursivo
	|	
	;
	'''
	@_('CONST declaracionConstanteRecursivo',
	'empty')
	def declaracionConstanteCONST(self, p):
		pass
		
	'''
	declaracionConstanteRecursivo : declaracionConstanteRecursivo declaracionConstante
	|	declaracionConstante
	|
	;
	'''
	@_('declaracionConstanteRecursivo declaracionConstante',
	'declaracionConstante',
	'empty')
	def declaracionConstanteRecursivo(self, p):
		pass
		
	'''
	declaracionVariableIN : "IN" declaracionVariableRecursivo
	|	
	;
	'''
	@_('IN declaracionVariableRecursivo',
	'empty')
	def declaracionVariableIN(self, p):
		pass
		
	'''
	declaracionVariableINOUT : "INOUT" declaracionVariableRecursivo
	|	
	;
	'''
	@_('INOUT declaracionVariableRecursivo',
	'empty')
	def declaracionVariableINOUT(self, p):
		pass
		
	'''
	declaracionVariableOUT : "OUT" declaracionVariableRecursivo
	|	
	;
	'''
	@_('OUT declaracionConstanteRecursivo',
	'empty')
	def declaracionVariableOUT(self, p):
		pass
	
	'''
	declaracionVariableVAR : "VAR" declaracionVariableRecursivo
	|	
	;
	'''
	@_('VAR declaracionVariableRecursivo', 'empty')
	def declaracionVariableVAR(self, p):
		pass
		
	'''
	sentenciaSecuenciaBEGIN : "BEGIN" sentenciaSecuencia
	|	
	;
	'''
	@_('BEGIN sentenciaSecuencia', 'empty')
	def sentenciaSecuenciaBEGIN(self, p):
		pass
		
	'''
	declaracionVariableRecursivo : declaracionVariableRecursivo declaracionVariable
	|	declaracionVariable
	|
	;
	'''
	@_('declaracionVariableRecursivo declaracionVariable',
	'declaracionVariable',
	'empty')
	def declaracionVariableRecursivo(self, p):
		pass
		
	'''
	tipoFormal : expresionCorchete2 "BIT"
	;
	'''
	@_('expresionCorchete2 BIT')
	def tipoFormal(self, p):
		pass
		
	'''
	expresionCorchete2 : expresionCorchete2 "[" expresionOpcional "]"
	|	"[" expresionOpcional "]"
	|
	;
	'''
	@_('expresionCorchete2 "[" expresionOpcional "]"',
	'"[" expresionOpcional "]"',
	'empty')
	def expresionCorchete2(self, p):
		pass
		
	'''
	expresionOpcional : expresion
	|	
	;
	'''
	@_('expresion',
	'empty')
	def expresionOpcional(self, p):
		pass
		
	'''
	tipoFormalBus : expresionCorchete2 "TS"
	|	expresionCorchete2 "OC"
	;
	'''
	@_('expresionCorchete2 TS', 'expresionCorchete2 OC')
	def tipoFormalBus(self, p):
		pass
		
	'''
	declaracionTipo : "TYPE" ID simboloPor listaIdParentesis ";" 
	declaracionConstanteCONST 
	tipoFormalIN
	tipoFormlINOUT
	declaracionVariableOUT 
	declaracionVariableVAR 
	sentenciaSecuenciaBEGIN 
	END ID
	;
	'''
	@_('TYPE ID simboloPor listaIdParentesis ";" declaracionConstanteCONST tipoFormalIN tipoFormlINOUT declaracionVariableOUT declaracionVariableVAR sentenciaSecuenciaBEGIN END ID')
	def declaracionTipo(self, p):
		pass
		
	'''
	simboloPor : "*"
	|	
	;
	'''
	@_('"*"',
	'empty')
	def simboloPor(self, p):
		pass
		
	'''
	listaIdParentesis : "(" listaId ")"
	|	
	;
	'''
	@_('"(" listaId ")"',
	'empty')
	def listaIdParentesis(self, p):
		pass
		
	'''
	tipoFormalIN : IN tipoFormallistaId
	|	
	;
	'''
	@_('IN tipoFormallistaId',
	'empty')
	def tipoFormalIN(self, p):
		pass
		
	'''
	tipoFormallistaId : tipoFormallistaId listaId ":" tipoFormal ";"
	|	listaId ":" tipoFormal ";"
	|
	;
	'''
	@_('tipoFormallistaId listaId ":" tipoFormal ";"',
	'listaId ":" tipoFormal ";"',
	'empty')
	def tipoFormallistaId(self, p):
		pass
		
	'''
	tipoFormnalINOUT : INOUT tipoFormlBuslistaId
	|	
	;
	'''
	@_('INOUT tipoFormallistaId',
	'empty')
	def tipoFormlINOUT(self, p):
		pass
		
	'''
	tipoFormlBuslistaId : tipoFormlBuslistaId listaId ":" tipoFormalBus ";"
	|	listaId ":" tipoFormalBus ";"
	|
	;
	'''
	@_('tipoFormlBuslistaId listaId ":" tipoFormalBus ";"',
	'listaId ":" tipoFormalBus ";"',
	'empty')
	def tipoFormlBuslistaId(self, p):
		pass
		
	'''
	assinacionUnidad : ID selector "(" listaExpresiones ")"
	'''
	@_('ID selector "(" listaExpresiones ")"')
	def asignacionUnidad(self, p):
		pass
	
	
	
	@_('')
	def empty(self, p):
		pass
		
if __name__ == '__main__':
	import sys
	lexer = CalcLexer()
	parser = CalcParser()
	if(len(sys.argv)!=2):#Verifica la cantidad de argumentos a la hora de compilar si no son 2. "py 'fichero.py' 'archivo'"
		sys.stderr.write('Usage: "{}" "filename"\n'.format(sys.argv[0]))#permite que al al compilar indique que debe de darse el archivo de la forma python.exe "fichero.py" "Archivo a abrir, como un simple print"
		raise SystemExit(1)#termina el programa
	file= open(sys.argv[1]).read()#en caso de que indique archivo tome el segundo string y abra el archivo y convierta con .read() a string
	maxLenthLine=0
	for linea in open(sys.argv[1]):
		if(maxLenthLine<len(linea)):
			maxLenthLine=len(linea)#verifica la columna maxima para el formato de centrado (visual en los print)
			print("malen",maxLenthLine)
	print("{:{align}{width}}".format("Archivo recibido - contenido inicio", align="^", width=maxLenthLine))
	print("-"*maxLenthLine)
	print(file)
	print("-"*maxLenthLine)
	print("{:{align}{width}}".format("Archivo recibido - contenido fin", align="^", width=maxLenthLine))
	
	#print("aplicando tokenize")
	lexer.fileName=sys.argv[1]
	parser.parse(lexer.tokenize(file))
