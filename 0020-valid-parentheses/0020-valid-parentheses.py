class Solution:
    def isValid(self, s: str) -> bool:
      pila=[]
      for caracter in s:
        if (caracter=='(')or (caracter=='[') or (caracter=='{'):
          pila.append(caracter)
        
        elif (caracter==')') or (caracter==']') or (caracter=='}'):
          if not pila:
            return False
          else:
            ultimocaracter=pila.pop()
            if (caracter==')' and ultimocaracter!='(')or(caracter==']' and ultimocaracter!='[')or(caracter=='}' and ultimocaracter!='{'):
                return False

      return not pila      