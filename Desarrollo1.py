import random, pygame, Pantalla

class Pokemon():
    def __init__(self,id,nombre,tipo,vida,vida_actual,precision,nivel,evasion,eficaz,diseno):
        self.id=id
        self.nombre=nombre
        self.tipo=tipo
        self.vida=vida
        self.vida_actual=vida_actual
        self.precision=precision
        self.nivel=nivel
        self.evasion=evasion
        self.eficaz=eficaz
        self.diseno=diseno

    def get_vida(self):
        return self.vida
    
    def get_vida_actual(self):
        return self.vida_actual

    def get_nombre(self):
        return self.nombre
    
    def get_diseno(self):
        return self.diseno
    
    def get_id(self):
        return self.id
    
    def get_eficaz(self):
        return self.eficaz
    
    def get_tipo(self):
        return self.tipo
    
    def set_vida_actual(self,dano):
        self.vida_actual=self.vida_actual-dano

    def set_escudo(self,dano,escu):
        if escu>0:
            dano=dano-escu
            self.vida_actual=self.vida_actual-dano

    def atacar(self):
        golpe=random.randint(1,self.nivel)*random.randint(1,self.precision)
        return golpe
    
    def defender(self):
        escudo=random.randint(1,self.evasion)
        return escudo
    
    def descripcion(self):
        return f'Nombre:{self.nombre}   Tipo:{self.tipo}    Nivel:{self.nivel}  Vida:{self.vida}/{self.vida_actual}    Precision:{self.precision}  Evasion:{self.evasion}  Es eficaz contra tipo:{self.eficaz}'

    def evolucion(self,energia):
        energia=energia+random.randint(1,5)
        return energia

class Fuego(Pokemon):
    def __init__(self, id, nombre, tipo, vida, vida_actual, precision, nivel, evasion, resistencia, diseno, energia_fuego):
        super().__init__(id, nombre, tipo, vida, vida_actual, precision, nivel, evasion, resistencia, diseno)
        self.energia_fuego=energia_fuego

    def especial(self):
        self.nivel=round(self.nivel*1.2)
        self.energia_fuego=self.energia_fuego-10
        print(self.nombre+"a usado Danza llama aumentando su nivel en un 20% ,gasto 10 de energia")

    def evolucion(self):
        suma=super().evolucion(self.energia_fuego)
        self.energia_fuego=self.energia_fuego+suma
        print(self.nombre," Evoluciono recuperando ",suma," de energia")

    def get_energia(self):
        return self.energia_fuego

class Agua(Pokemon):
    def __init__(self, id, nombre, tipo, vida,  vida_actual, precision, nivel, evasion, resistencia, diseno, energia_agua):
        super().__init__(id, nombre, tipo, vida,  vida_actual, precision, nivel, evasion ,resistencia, diseno)
        self.energia_agua=energia_agua

    def especial(self):
        self.precision=self.precision+10
        self.energia_agua=self.energia_agua-10
        print(self.nombre,"a usado Aqua jet aumentando su presicion en 10, gasto 10 de energia")

    def evolucion(self):
        suma=super().evolucion(self.energia_agua)
        self.energia_agua=self.energia_agua+suma
        print(self.nombre," Evoluciono recuperando ",suma," de energia")

    def get_energia(self):
        return self.energia_agua

class Planta(Pokemon):
    def __init__(self, id, nombre, tipo, vida,  vida_actual, precision, nivel, evasion, resistencia, diseno, energia_planta):
        super().__init__(id, nombre, tipo, vida,  vida_actual, precision, nivel, evasion, resistencia, diseno)
        self.energia_planta=energia_planta

    def especial(self):
        self.evasion=self.evasion+7
        self.energia_planta=self.energia_planta-10
        print(self.nombre+"a usado Ciclon de hojas aumentando su evacion en 5, gasto 10 de energia")

    def evolucion(self):
        suma=super().evolucion(self.energia_planta)
        self.energia_planta=self.energia_planta+suma
        print(self.nombre," Evoluciono recuperando ",suma," de energia")

    def get_energia(self):
        return self.energia_planta

def estadisticas(Dicc: dict, op, scre, fon, cont, dis):
    x=Pantalla.ingresar_nombre(scre,fon,dis)
    Nombre=x.nombre_run()
    id=cont
    vida=random.randint(170,200)
    vida_a=vida
    precision=random.randint(4,9)
    nivel=random.randint(5,10)
    evasion=random.randint(3,7)
    energia=random.randint(20,25)
    diseno=dis
    if op==1:
        tipo="Fuego"
        eficaz="Planta"
        Dicc[id]=Fuego(id,Nombre,tipo,vida,vida_a,precision,nivel,evasion,eficaz,diseno,energia)
    elif op==2:
        tipo="Agua"
        eficaz="Fuego"
        Dicc[id]=Agua(id,Nombre,tipo,vida,vida_a,precision,nivel,evasion,eficaz,diseno,energia)
    elif op==3:
        tipo="Planta"
        eficaz="Agua"
        Dicc[id]=Planta(id,Nombre,tipo,vida,vida_a,precision,nivel,evasion,eficaz,diseno,energia)
    print(Dicc[id].descripcion())

def Pelea_pokemon(Jugador1: dict,Jugador2: dict,screen):
    elecciones=["Atacar","Especial","Defenderse","Evolucionar","Descripcion","Cambiar Pokemon"]
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Sonidos\Pelea.mp3')
    pygame.mixer.music.play(-1)
    Escenario=pygame.image.load('Sprites\escenario.jpg')
    Combate=Pantalla.Pelea(screen,elecciones,Escenario)
    Combate.Pelea_menu(Jugador1,Jugador2,1,4)

def Elecciones(J_1:dict,J_2:dict,Opcion1,Opcion2,ID1,ID2):
    print("Op1:",Opcion1)
    print("Op2:",Opcion2)

    texto=""
    nombre1=J_1[ID1].get_nombre()
    nombre2=J_2[ID2].get_nombre()
    eficaz1=J_1[ID1].get_eficaz()
    eficaz2=J_2[ID2].get_eficaz()
    tipo1=J_1[ID1].get_tipo()
    tipo2=J_2[ID2].get_tipo()

    if Opcion1=="Atacar":
        dano1=J_1[ID1].atacar()
        if eficaz1==tipo2:
            dano1=dano1+10
            texto="el daño aumento al ser eficaz contra ese tipo"
        J_2[ID2].set_vida_actual(dano1)
        print(nombre1," ataco a ",nombre2,", Causandole",dano1,"de daño",texto)
    elif Opcion1=="Especial":
        J_1[ID1].especial()
    elif Opcion1=="Defenderse":
        prote=J_1[ID1].defender()
    elif Opcion1=="Evolucionar":
        J_1[ID1].evolucion()

    texto=""
    if Opcion2=="Atacar":
        dano2=J_2[ID2].atacar()
        if eficaz2==tipo1:
            dano2=dano2+10
            texto="el daño aumento al ser eficaz contra ese tipo"
        J_1[ID1].set_vida_actual(dano2)
        print(nombre2," ataco a ",nombre1,", Causandole",dano2,"de daño",texto)
    elif Opcion2=="Especial":
        J_2[ID2].especial()
    elif Opcion2=="Defenderse":
        prote2=J_2[ID2].defender()
    elif Opcion2=="Evolucionar":
        J_2[ID2].evolucion()

    if Opcion1=="Defenderse" and Opcion2=="Atacar":
        J_1[ID1].set_escudo(dano2,prote)
        print(nombre1," se defendio reduciendo el daño en ",prote)

    if Opcion1=="Atacar" and Opcion2=="Defenderse":
        J_2[ID2].set_escudo(dano1,prote2)
        print("Pero",nombre2," se defendio reduciendo el daño en ",prote2)

    if Opcion1=="Cambiar Pokemon" and Opcion2=="Atacar":
        J_1[ID1].set_vida_actual(dano2)

    if Opcion1=="Atacar" and Opcion2=="Cambiar Pokemon":
        J_2[ID2].set_vida_actual(dano1)

def main():
    pygame.init()                                                   #Se inicializa pygame
    pygame.mixer.init()                                             #Se inicializa pygame mixer que se usa para la musica
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Sonidos\sonido1.mp3')                  #Se guarda la cancion que va a ser mi musica de inicio y seleccion de pokemones
    pygame.mixer.music.set_volume(0.1)                              #Se ajusta el volumen
    pygame.mixer.music.play(-1)                                     #Se reproduce la cancion y tiene un valor de -1 el cual hara que se reproduzca en bucle |0=una vez| |numero mayor a 0, la cantidad mas 1|
    Inicio=pygame.image.load('Sprites\Inicio.jpg')                  #Se guarda un la imagen que voy a usar como fondo en una variable
    screen=pygame.display.set_mode((1280,720))
    options = ["1. Iniciar pelea pokemon","2. Exit"]                #Arreglo que contiene las opciones de mi menu
    menu=Pantalla.Menu(screen, options, Inicio)                     #Se crea un objeto de tipo menu
    menu.run()                                                      #Se inicia el menu
    pygame.quit()                                                   #Se cierra el programa

if __name__ == "__main__":
    main()