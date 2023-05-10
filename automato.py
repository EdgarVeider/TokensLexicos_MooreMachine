from automata.fa.Moore import Moore

estados = ['q0', 'INT-i', 'INT-n', 'INT-t', 'INT-*',
            'ID', 'ID*', 'ID_LPAREN', 'LRPAREN',
            'RETURN_R','RETURN_E', 'RETURN_T', 'RETURN_U', 'RETURN_R2', 'RETURN_E', 'RETURN_N', 'RETURN_*', 'RETURN_RPAREN',
            'VOID_V', 'VOID_O', 'VOID_I', 'VOID_D', 'VOID_)', 'VOID_*', 'VOID_RPAREN_LBRACES']

lenguage = ['a','b','c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0','1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '<', '>', '=']
saidas = ['INT']

moore = Moore(estados,
              lenguage,
              saidas,
              {
                #ESTADO INICIAL
                'q0':{
                    'i' : 'INT-i',          #int
                    'v' : 'VOID_V',         #VOID
                    'r' : 'RETURN_R',       #return
                    ' ' : 'q0',             #FICA EM LOOP QUANDO RE
                    '}' : 'RBRACES',

                    'a' : 'ID',
                    'b' : 'ID',
                    'c' : 'ID',
                    'd' : 'ID',
                    'e' : 'ID',
                    'f' : 'ID',
                    'g' : 'ID',
                    'h' : 'ID', 
                    'j' : 'ID', 
                    'k' : 'ID', 
                    'l' : 'ID', 
                    'm' : 'ID', 
                    'n' : 'ID',
                    'o' : 'ID', 
                    'p' : 'ID', 
                    'q' : 'ID', 
                    's' : 'ID', 
                    't' : 'ID', 
                    'u' : 'ID', 
                    'w' : 'ID', 
                    'y' : 'ID', 
                    'z' : 'ID', 
                },
                #------------------I N T-------------------------
                'INT-i':{
                    'n' : 'INT-n'
                },

                'INT-n':{
                    't' : 'INT-t'
                },

                'INT-t':{
                    ' ' : 'INT-*'
                },

                'INT-*':{
                    'a' : 'q0',
                    'b' : 'q0',
                    'c' : 'q0',
                    'd' : 'q0',
                    'e' : 'q0',
                    'f' : 'q0',
                    'g' : 'q0',
                    'h' : 'q0', 
                    'j' : 'q0', 
                    'k' : 'q0', 
                    'l' : 'q0', 
                    'm' : 'q0', 
                    'n' : 'q0',
                    'o' : 'q0', 
                    'p' : 'q0', 
                    'q' : 'q0', 
                    'r' : 'q0', 
                    's' : 'q0', 
                    't' : 'q0', 
                    'u' : 'q0', 
                    'v' : 'q0', 
                    'w' : 'q0', 
                    'y' : 'q0', 
                    'z' : 'q0', 

                },

                #------------------I D E N T I F I C A D O R-------------------------
                'ID':{
                    'a' : 'ID',
                    'b' : 'ID',
                    'c' : 'ID',
                    'd' : 'ID',
                    'e' : 'ID',
                    'f' : 'ID',
                    'g' : 'ID',
                    'h' : 'ID', 
                    'i' : 'ID',
                    'j' : 'ID', 
                    'k' : 'ID', 
                    'l' : 'ID', 
                    'm' : 'ID', 
                    'n' : 'ID',
                    'o' : 'ID', 
                    'p' : 'ID', 
                    'q' : 'ID', 
                    'r' : 'ID', 
                    's' : 'ID', 
                    't' : 'ID', 
                    'u' : 'ID', 
                    'v' : 'ID', 
                    'w' : 'ID', 
                    'y' : 'ID', 
                    'z' : 'ID', 

                    ' ' : 'ID*',
                    '(' : 'ID_LPAREN'
                },

                'ID_LPAREN':{
                    'v': 'VOID_V',
                    'i': 'INT_N',
                    ')': 'LRPAREN'
                },
                
                'ID*':{
                    
                },

                #------------------V O I D-------------------------

                'VOID_V':{
                    'o' : 'VOID_O',

                    'a' : 'ID',
                    'b' : 'ID',
                    'c' : 'ID',
                    'd' : 'ID',
                    'e' : 'ID',
                    'f' : 'ID',
                    'g' : 'ID',
                    'h' : 'ID', 
                    'i' : 'ID',
                    'j' : 'ID', 
                    'k' : 'ID', 
                    'l' : 'ID', 
                    'm' : 'ID', 
                    'n' : 'ID',
                    'p' : 'ID', 
                    'q' : 'ID', 
                    'r' : 'ID', 
                    's' : 'ID', 
                    't' : 'ID', 
                    'u' : 'ID', 
                    'v' : 'ID', 
                    'w' : 'ID', 
                    'y' : 'ID', 
                    'z' : 'ID', 
                },

                'VOID_O':{
                    'i' : 'VOID_I',

                    'a' : 'ID',
                    'b' : 'ID',
                    'c' : 'ID',
                    'd' : 'ID',
                    'e' : 'ID',
                    'f' : 'ID',
                    'g' : 'ID',
                    'h' : 'ID', 
                    'j' : 'ID', 
                    'k' : 'ID', 
                    'l' : 'ID', 
                    'm' : 'ID', 
                    'n' : 'ID',
                    'o' : 'ID',
                    'p' : 'ID', 
                    'q' : 'ID', 
                    'r' : 'ID', 
                    's' : 'ID', 
                    't' : 'ID', 
                    'u' : 'ID', 
                    'v' : 'ID', 
                    'w' : 'ID', 
                    'y' : 'ID', 
                    'z' : 'ID', 
                },

                'VOID_I':{
                    'd' : 'VOID_D',

                    'a' : 'ID',
                    'b' : 'ID',
                    'c' : 'ID',
                    'e' : 'ID',
                    'f' : 'ID',
                    'g' : 'ID',
                    'h' : 'ID', 
                    'i' : 'ID', 
                    'j' : 'ID', 
                    'k' : 'ID', 
                    'l' : 'ID', 
                    'm' : 'ID', 
                    'n' : 'ID',
                    'o' : 'ID',
                    'p' : 'ID', 
                    'q' : 'ID', 
                    'r' : 'ID', 
                    's' : 'ID', 
                    't' : 'ID', 
                    'u' : 'ID', 
                    'v' : 'ID', 
                    'w' : 'ID', 
                    'y' : 'ID', 
                    'z' : 'ID', 
                },

                
                'VOID_D':{
                    ' ' : 'VOID_*',
                    ')' : 'VOID_)',

                    'a' : 'ID',
                    'b' : 'ID',
                    'c' : 'ID',
                    'e' : 'ID',
                    'f' : 'ID',
                    'g' : 'ID',
                    'h' : 'ID', 
                    'i' : 'ID', 
                    'j' : 'ID', 
                    'k' : 'ID', 
                    'l' : 'ID', 
                    'm' : 'ID', 
                    'n' : 'ID',
                    'o' : 'ID',
                    'p' : 'ID', 
                    'q' : 'ID', 
                    'r' : 'ID', 
                    's' : 'ID', 
                    't' : 'ID', 
                    'u' : 'ID', 
                    'v' : 'ID', 
                    'w' : 'ID', 
                    'y' : 'ID', 
                    'z' : 'ID', 
                },
                
                'VOID_)':{
                    '{' : 'VOID_RPAREN_LBRACES'
                },

                'VOID_RPAREN_LBRACES':{
                    ' ' : 'q0',

                    'a' : 'ID',
                    'b' : 'ID',
                    'c' : 'ID',
                    'e' : 'ID',
                    'f' : 'ID',
                    'g' : 'ID',
                    'h' : 'ID', 
                    'i' : 'ID', 
                    'j' : 'ID', 
                    'k' : 'ID', 
                    'l' : 'ID', 
                    'm' : 'ID', 
                    'n' : 'ID',
                    'o' : 'ID',
                    'p' : 'ID', 
                    'q' : 'ID', 
                    'r' : 'ID', 
                    's' : 'ID', 
                    't' : 'ID', 
                    'u' : 'ID', 
                    'v' : 'ID', 
                    'w' : 'ID', 
                    'y' : 'ID', 
                    'z' : 'ID',
                },
                
                #------------------R E T U R N-------------------------

                'RETURN_R':{
                    'e' : 'RETURN_E',

                    'a' : 'ID',
                    'b' : 'ID',
                    'c' : 'ID',
                    'f' : 'ID',
                    'g' : 'ID',
                    'h' : 'ID', 
                    'i' : 'ID', 
                    'j' : 'ID', 
                    'k' : 'ID', 
                    'l' : 'ID', 
                    'm' : 'ID', 
                    'n' : 'ID',
                    'o' : 'ID',
                    'p' : 'ID', 
                    'q' : 'ID', 
                    'r' : 'ID', 
                    's' : 'ID', 
                    't' : 'ID', 
                    'u' : 'ID', 
                    'v' : 'ID', 
                    'w' : 'ID', 
                    'y' : 'ID', 
                    'z' : 'ID',
                },

                'RETURN_E':{
                    't' : 'RETURN_T',

                    'a' : 'ID',
                    'b' : 'ID',
                    'c' : 'ID',
                    'e' : 'ID',
                    'f' : 'ID',
                    'g' : 'ID',
                    'h' : 'ID', 
                    'i' : 'ID', 
                    'j' : 'ID', 
                    'k' : 'ID', 
                    'l' : 'ID', 
                    'm' : 'ID', 
                    'n' : 'ID',
                    'o' : 'ID',
                    'p' : 'ID', 
                    'q' : 'ID', 
                    'r' : 'ID', 
                    's' : 'ID',  
                    'u' : 'ID', 
                    'v' : 'ID', 
                    'w' : 'ID', 
                    'y' : 'ID', 
                    'z' : 'ID',
                },
                'RETURN_T':{
                    'u' : 'RETURN_U',

                    'a' : 'ID',
                    'b' : 'ID',
                    'c' : 'ID',
                    'e' : 'ID',
                    'f' : 'ID',
                    'g' : 'ID',
                    'h' : 'ID', 
                    'i' : 'ID', 
                    'j' : 'ID', 
                    'k' : 'ID', 
                    'l' : 'ID', 
                    'm' : 'ID', 
                    'n' : 'ID',
                    'o' : 'ID',
                    'p' : 'ID', 
                    'q' : 'ID', 
                    'r' : 'ID', 
                    's' : 'ID', 
                    't' : 'ID', 
                    'v' : 'ID', 
                    'w' : 'ID', 
                    'y' : 'ID', 
                    'z' : 'ID',
                },
                'RETURN_U':{
                    'r' : 'RETURN_R2',

                    'a' : 'ID',
                    'b' : 'ID',
                    'c' : 'ID',
                    'e' : 'ID',
                    'f' : 'ID',
                    'g' : 'ID',
                    'h' : 'ID', 
                    'i' : 'ID', 
                    'j' : 'ID', 
                    'k' : 'ID', 
                    'l' : 'ID', 
                    'm' : 'ID', 
                    'n' : 'ID',
                    'o' : 'ID',
                    'p' : 'ID', 
                    'q' : 'ID', 
                    's' : 'ID', 
                    't' : 'ID', 
                    'u' : 'ID', 
                    'v' : 'ID', 
                    'w' : 'ID', 
                    'y' : 'ID', 
                    'z' : 'ID',
                },

                'RETURN_R2':{
                    'n' : 'RETURN_N',

                    'a' : 'ID',
                    'b' : 'ID',
                    'c' : 'ID',
                    'e' : 'ID',
                    'f' : 'ID',
                    'g' : 'ID',
                    'h' : 'ID', 
                    'i' : 'ID', 
                    'j' : 'ID', 
                    'k' : 'ID', 
                    'l' : 'ID', 
                    'm' : 'ID', 
                    'o' : 'ID',
                    'p' : 'ID', 
                    'q' : 'ID', 
                    'r' : 'ID', 
                    's' : 'ID', 
                    't' : 'ID', 
                    'u' : 'ID', 
                    'v' : 'ID', 
                    'w' : 'ID', 
                    'y' : 'ID', 
                    'z' : 'ID',
                },

                'RETURN_N':{
                    ' ' : 'RETURN_*',
                    '(' : 'RETURN_LPAREN',

                    'a' : 'ID',
                    'b' : 'ID',
                    'c' : 'ID',
                    'e' : 'ID',
                    'f' : 'ID',
                    'g' : 'ID',
                    'h' : 'ID', 
                    'i' : 'ID', 
                    'j' : 'ID', 
                    'k' : 'ID', 
                    'l' : 'ID', 
                    'm' : 'ID', 
                    'n' : 'ID',
                    'o' : 'ID',
                    'p' : 'ID', 
                    'q' : 'ID', 
                    'r' : 'ID', 
                    's' : 'ID', 
                    't' : 'ID', 
                    'u' : 'ID', 
                    'v' : 'ID', 
                    'w' : 'ID', 
                    'y' : 'ID', 
                    'z' : 'ID',

                },

                'RETURN_LPAREN':{
                    '0' : "NUMBER",
                    '1' : "NUMBER",
                    '2' : "NUMBER",
                    '3' : "NUMBER",
                    '4' : "NUMBER",
                    '5' : "NUMBER",
                    '6' : "NUMBER",
                    '7' : "NUMBER",
                    '8' : "NUMBER",
                    '9' : "NUMBER",
                },

            #------------------NUMBER-------------------------

                'NUMBER':{
                    '0' : "NUMBER",
                    '1' : "NUMBER",
                    '2' : "NUMBER",
                    '3' : "NUMBER",
                    '4' : "NUMBER",
                    '5' : "NUMBER",
                    '6' : "NUMBER",
                    '7' : "NUMBER",
                    '8' : "NUMBER",
                    '9' : "NUMBER",
                    
                    ')' : "NUMBER_RPAREN",
                },

                'NUMBER_RPAREN':{
                    ';' : "SEMICOLON",
                },

            #------------------S E M I C O L O N-------------------------

                'SEMICOLON':{
                    ' ' : "q0",
                },

            #------------------B R A C E S-------------------------------

                'RBRACES':{
                    
                }
              },



            #------------------S A I D A S------------------------------

              'q0',
              {
                'INT-*': "INT\n",
                'ID*'  :"ID\n",
                'ID_LPAREN' : "ID\nLPAREN\n",
                'LRPAREN' : "ID\nLPAREN\nRPAREN\n",
                'VOID_)': "VOID\nRPAREN",
                'VOID_RPAREN_LBRACES':"VOID\nRPAREN\nLBRACES\n",
                'VOID_*': "VOID\n",
                'RETURN_*' : "RETURN\n",
                'RETURN_LPAREN' : "RETURN\nLPAREN\n",
                'NUMBER_RPAREN' : "NUMBER\nRPAREN\n",
                'SEMICOLON': "SEMICOLON\n",
                'RBRACES': "RBRACES",


                'q0'   : "",
                'INT-i': "",
                'INT-n': "",
                'INT-t': "",
                'ID'  : "",
                'VOID_V': "",
                'VOID_O': "",
                'VOID_I': "",
                'VOID_D': "",
                'RETURN_R':"",
                'RETURN_E':"",
                'RETURN_T':"",
                'RETURN_U':"",
                'RETURN_R2':"",
                'RETURN_N':"",
                'NUMBER':"",
              }
              )



print(moore.get_output_from_string('int main(void){  return(32);  }'))

