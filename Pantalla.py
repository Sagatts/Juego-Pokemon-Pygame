import pygame , sys, Desarrollo1

class Menu():
    def __init__(self, screen, options , fondo):                                            #Se establece la clase menu el cual recibe el objeto, la pantalla, las opciones y el fondo
        self.screen = screen                                                                #Pantalla
        self.options = options                                                              #Opciones
        self.font = pygame.font.Font(None, 36)                                              #Fuente de texto con un tamano de 36 pixeles
        self.selected_option = 0                                                            #opcion seleccionado se inicia en 0
        self.fondo=fondo                                                                    #Fondo

    def draw_menu(self):                                                                    #Metodo Mostrar el menu en pantalla
        for i, option in enumerate(self.options):                                           #Se recorren las opciones con la funcion enumerate
            text = self.font.render(option, True, (255, 255, 255))                          #La variable text tiene las opciones y el color del texto del menu
            rect = text.get_rect(center=(self.screen.get_width() // 2, 200 + i * 60))       #La variable rect es el rectangulo que cubre la opcion actual| get_width se obtiene la mitad de la pantalla
            if i == self.selected_option:                                                   #Si la opcion actual es la opcion seleccionada entra el if y
                pygame.draw.rect(self.screen, (128, 128, 128), rect.inflate(10, 10))        #dibuja un rectangulo verde en la opciones que se esta actualmente aumentando un poco el rectangulo
            self.screen.blit(text, rect)                                                    #Se muestra en pantalla las opciones y el rectangulo que va a cubrir esta opcion

    def run(self):                                                                          #Metodo run
        running = True                                                                      #Variable que va a ser igual a True
        while running:                                                                      #Empieza el bucle
            for event in pygame.event.get():                                                #for en donde estaran todos los eventos tengo mi evento y mi funcion que tomara este evento
                if event.type == pygame.QUIT:                                               #si se apreta la X se cerrara el programa
                    salir(self.screen)                                                          #Cierra le ventana
                elif event.type == pygame.KEYDOWN:                                              #Si el tipo de evento es igual cuando se presiona una tecla
                    if event.key == pygame.K_UP:                                                #Si el evento es igual a flecha para arriba se va a la opcion de arriba
                        self.selected_option = (self.selected_option - 1) % len(self.options)   #se usan el len para tener el largo de las opciones y se saca el modulo para que no se salga del rango
                    elif event.key == pygame.K_DOWN:                                            #Si el evento es igual a flecha para abajo se va a la opcion de abajo
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:                                          #Si el evento es igual a ENTER
                        selected_action = self.options[self.selected_option]                    #variable que guarda la opciones seleccionada
                        if selected_action=="2. Exit":                                          #Si es igual a 2.Exit cierra el programa
                            running=False
                        elif selected_action=="1. Iniciar pelea pokemon":                       #Si es igual a 1.Pelea va a la funcion seleccionar pokemon
                            Seleccionar_Pokemones(self.screen, self.options, self.fondo)

            self.screen.blit(self.fondo,(0,0))                                                  #En la pantalla coloca el fondo
            self.draw_menu()                                                                    #Se llama al metodo draw menu
            pygame.display.flip()                                                               #Actualiza la ventana

class menu_pokemones(Menu):
    def __init__(self, screen, options, fondo, tipos):
        super().__init__(screen, options, fondo)
        self.tipos=tipos
        self.J1={}
        self.J2={}
    
    def draw_menu(self,cont):                                                                                                               #Mostrar el menu en pantalla
        for i, option in enumerate(self.tipos):                                                                                             #Se recorren las opciones con la funcion enumerate
            text = self.font.render(option, True, (255, 255, 255))                                                                          #La variable text tiene las opciones y el color del texto del menu
            rect = text.get_rect(center=(self.screen.get_width() // 2, 200 + i * 60))                                                       #La variable rect es el rectangulo que cubre la opcion actual
            if cont<4:
                draw_text("Jugador 1 Escoge el tipo de tu pokemon:",pygame.font.SysFont("arialblack",20),(255,255,255),450,100,self.screen)   #Se llama la funcion draw text que mostrara en pantalla el texto y este tiene su formato,su colo,su ubicacion y la pantalla
            elif cont>=4 and cont<7:
                draw_text("Jugador 2 Escoge el tipo del pokemon:",pygame.font.SysFont("arialblack",20),(255,255,255),450,100,self.screen)
            if i == self.selected_option:                                                                                                   #Si la opcion actual es la opcion seleccionada entra el if y
                pygame.draw.rect(self.screen, (128, 128, 128), rect.inflate(10, 10))                                                        #dibuja un rectangulo verde en la opciones que se esta actualmente
            self.screen.blit(text, rect)                                                                                                    #Se muestra en pantalla las opciones

    def poke_run(self):
        running = True
        cont=1
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir(self.screen)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.tipos)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.tipos)
                    elif event.key == pygame.K_RETURN:
                        selected_action = self.tipos[self.selected_option]
                        if cont<4:
                            if selected_action=="1.Fuego":
                                diseno=pygame.image.load('Sprites\Fuego2.png')
                                Desarrollo1.estadisticas(self.J1,1,self.screen,self.fondo,cont,diseno)
                            elif selected_action=="2.Agua":
                                diseno=pygame.image.load('Sprites\Agua2.png')
                                Desarrollo1.estadisticas(self.J1,2,self.screen,self.fondo,cont,diseno)
                            elif selected_action=="3.Planta":
                                diseno=pygame.image.load('Sprites\Planta2.png')
                                Desarrollo1.estadisticas(self.J1,3,self.screen,self.fondo,cont,diseno)
                            cont=cont+1
                        elif cont>=4 and cont<7:
                            if selected_action=="1.Fuego":
                                diseno=pygame.image.load('Sprites\Fuego.png')
                                Desarrollo1.estadisticas(self.J2,1,self.screen,self.fondo,cont,diseno)
                            elif selected_action=="2.Agua":
                                diseno=pygame.image.load('Sprites\Agua.png')
                                Desarrollo1.estadisticas(self.J2,2,self.screen,self.fondo,cont,diseno)
                            elif selected_action=="3.Planta":
                                diseno=pygame.image.load('Sprites\Planta.png')
                                Desarrollo1.estadisticas(self.J2,3,self.screen,self.fondo,cont,diseno)
                            cont=cont+1
                        if cont==7:
                            print("Inicia la pelea")
                            Desarrollo1.Pelea_pokemon(self.J1,self.J2,self.screen)
            
            self.screen.blit(self.fondo,(0,0))
            self.draw_menu(cont)
            pygame.display.flip()

class ingresar_nombre():
    def __init__(self, screen, fondo, diseno):
        self.font=pygame.font.Font(None, 36)
        self.screen=screen
        self.fondo=fondo
        self.diseno=diseno

    def draw_menu(self,name):
        text = self.font.render("Ingrese el nombre de su pokemon:"+name,True, (255, 255, 255))          #se guarda el texto
        self.screen.blit(self.diseno,(800,400))                                                         #Muesta la foto del diseno del tipo               
        self.screen.blit(text,(100,300))                                                                #Muesta el texto en pantalla

    def nombre_run(self):
        name=""                                                                                         #Se inicia una variable vacia
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir(self.screen)
                elif evento.type == pygame.KEYDOWN:                         #Evento presionar
                    if evento.key == pygame.K_BACKSPACE:                    #se apreta el backspace se borra una caracter
                        name = name[:-1]                    
                    elif evento.key == pygame.K_RETURN:                     #se apreta el enter para confirmar el nombre
                        return name
                    else:                                                   #cualquier otro evento se agrega el nombre
                        if len(name)<20 and evento.unicode.isalpha():
                            name += evento.unicode          

            self.screen.blit(self.fondo,(0,0))
            self.draw_menu(name)
            pygame.display.flip()

class Pelea(Menu):
    def __init__(self, screen, options, fondo):
        super().__init__(screen, options, fondo)

    def draw_menu(self,conta,vida_1,vida_2,vida_ac1,vida_ac2,nombre_1,nombre_2,dis_1,dis_2,energia_1,energia_2):
        vida_ac1=str(vida_ac1)
        vida_ac2=str(vida_ac2)
        energia_1=str(energia_1)
        energia_2=str(energia_2)
        for i, option in enumerate(self.options):
            text = self.font.render(option, True, (255, 255, 255))
            rect = text.get_rect(midleft=(self.screen.get_width() // 2 // 2 // 2 // 1.1 + i *160, 640))
            draw_text(nombre_1,pygame.font.SysFont("arialblack",20),(0,0,0),450,140,self.screen)
            draw_text(vida_1+" / "+vida_ac1,pygame.font.SysFont("arialblack",20),(0,0,0),450,170,self.screen)
            draw_text("Energia: "+energia_1,pygame.font.SysFont("arialblack",20),(0,0,0),450,200,self.screen)

            draw_text(nombre_2,pygame.font.SysFont("arialblack",20),(0,0,0),800,140,self.screen)
            draw_text(vida_2+" / "+vida_ac2,pygame.font.SysFont("arialblack",20),(0,0,0),800,170,self.screen)
            draw_text("Energia: "+energia_2,pygame.font.SysFont("arialblack",20),(0,0,0),800,200,self.screen)
            if conta==1:
                draw_text("Turno Jugador 1:",pygame.font.SysFont("arialblack",20),(0,0,0),450,100,self.screen)
            elif conta>=1:
                draw_text("Turno Jugador 2:",pygame.font.SysFont("arialblack",20),(0,0,0),750,100,self.screen)
            if i == self.selected_option:
                pygame.draw.rect(self.screen, (128, 128, 128), rect.inflate(10, 10))
            self.screen.blit(dis_1,(200,250))
            self.screen.blit(dis_2,(750,250))
            self.screen.blit(text, rect)                                                              

    def Pelea_menu(self,Juga1:dict,Juga2:dict,id1,id2):
        running = True
        cont=1
        fond=pygame.image.load("Sprites\Cambio Pokemon.jpg")
        numero_poke=["Pokemon 1","Pokemon 2","Pokemon 3"]
        seleccion=cambio_pokemon(self.screen,numero_poke,fond)
        cantidad_poke1=3
        cantidad_poke2=3
        victoria_1=""
        victoria_2=""
        while running:
            vida1=str(Juga1[id1].get_vida())
            vida2=str(Juga2[id2].get_vida())
            nombre1=Juga1[id1].get_nombre()
            nombre2=Juga2[id2].get_nombre()
            diseno1=Juga1[id1].get_diseno()
            diseno2=Juga2[id2].get_diseno()
            descrip1=Juga1[id1].descripcion()
            descrip2=Juga2[id2].descripcion()  
            vida_actual1=Juga1[id1].get_vida_actual()
            vida_actual2=Juga2[id2].get_vida_actual()
            id_uno=Juga1[id1].get_id()
            id_dos=Juga2[id2].get_id()
            energia1=Juga1[id1].get_energia()
            energia2=Juga2[id2].get_energia()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir(self.screen)
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif evento.key == pygame.K_RIGHT:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif evento.key == pygame.K_RETURN:
                        selected_action = self.options[self.selected_option]
                        if cont==1:
                            if selected_action=="Descripcion":
                                mostrar_descripcion(self.screen,descrip1,diseno1)
                                cont=1
                            elif selected_action=="Cambiar Pokemon":
                                op=1
                                id1=seleccion.cambio_pokemon(Juga1,op,id_uno)
                                if id1==0:
                                    print("")
                                    id1=id_uno
                                else:
                                    Opcion1=selected_action
                                    cont=cont+1
                            elif selected_action=="Especial":
                                if energia1<10:
                                    print("No puedes usar el especial, te falta energia usa evolucion para recargar")
                                else:
                                    Opcion1=selected_action
                                    cont=cont+1
                            else:
                                Opcion1=selected_action
                                cont=cont+1
                        elif cont==2:
                            if selected_action=="Descripcion":
                                mostrar_descripcion(self.screen,descrip2,diseno2)
                                cont=2
                            elif selected_action=="Cambiar Pokemon":
                                op=2
                                id2=seleccion.cambio_pokemon(Juga2,op,id_dos)
                                if id2==0:
                                    print("")
                                    id2=id_dos
                                else:
                                    Opcion2=selected_action
                                    cont=cont+1
                            elif selected_action=="Especial":
                                if energia2<10:
                                    print("No puedes usar el especial, te falta energia usa evolucion para recargar")
                                else:
                                    Opcion2=selected_action
                                    cont=cont+1
                            else:
                                Opcion2=selected_action
                                cont=cont+1
                        if cont==3:
                            Desarrollo1.Elecciones(Juga1,Juga2,Opcion1,Opcion2,id1,id2)
                            cont=1
                elif vida_actual1<=0 and cantidad_poke1>=0:
                    op=1
                    print(nombre1,"se debilito escoge otro pokemon")
                    cantidad_poke1=cantidad_poke1-1
                    if cantidad_poke1==0:
                        victoria_2="Gano el jugador 2"
                        victoria(self.screen,victoria_2)
                    id1=seleccion.cambio_pokemon(Juga1,op,id_uno)
                    cont=1

                elif vida_actual2<=0 and cantidad_poke2>=0:
                    op=2
                    print(nombre2,"se debilito escoge otro pokemon")
                    cantidad_poke2=cantidad_poke2-1
                    if cantidad_poke2==0: 
                        victoria_1="Gano el jugador 1"
                        victoria(self.screen,victoria_1)
                    id2=seleccion.cambio_pokemon(Juga2,op,id_dos)
                    cont=2

            self.screen.blit(self.fondo,(0,0))
            self.draw_menu(cont,vida1,vida2,vida_actual1,vida_actual2,nombre1,nombre2,diseno1,diseno2,energia1,energia2)
            pygame.display.flip()

def Seleccionar_Pokemones(scre, option, fon):
    tipos_de_pokemon=["1.Fuego","2.Agua","3.Planta"]
    menu_poke=menu_pokemones(scre, option, fon,tipos_de_pokemon)
    menu_poke.poke_run()

def mostrar_descripcion(scren,descripcion,diseno):
    running=True
    fondo_de=pygame.image.load("Sprites\Descripcion.JPG")
    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salir(scren)
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    running=False

            scren.blit(fondo_de,(0,0))
            scren.blit(diseno,(450,300))
            draw_text(descripcion,pygame.font.SysFont("arialblack",20),(0,0,0),0,600,scren)
            draw_text("Press Enter para volver",pygame.font.SysFont("arialblack",20),(0,0,0),0,0,scren)
            pygame.display.flip()

class cambio_pokemon(Menu):
    def __init__(self, screen, options, fondo):
        super().__init__(screen, options, fondo)

    def draw_menu(self,Pokemons: dict,id):
        for i, clave in enumerate(list(Pokemons.keys())[:3]):
            option=str(i+1)                                   
            text = self.font.render("Pokemon "+option, True, (255, 255, 255))                          
            rect = text.get_rect(midleft=(self.screen.get_width() // 2 // 2 , 90 + i * 200))
            draw_text("Press Atras para volver:",pygame.font.SysFont("arialblack",20),(255,255,255),0,0,self.screen)
            if id==1:
                draw_text("Jugador 1 Escoge:",pygame.font.SysFont("arialblack",20),(255,255,255),0,60,self.screen)
            elif id==4:
                draw_text("Jugador 2 Escoge:",pygame.font.SysFont("arialblack",20),(255,255,255),0,60,self.screen)
            diseno_poke=Pokemons[clave].get_diseno()
            diseno_p=pygame.transform.scale(diseno_poke,(250,200))
            nombres_poke=Pokemons[clave].get_nombre()
            vida_total=str(Pokemons[clave].get_vida())
            vida_actual=str(Pokemons[clave].get_vida_actual())
            draw_text(nombres_poke,pygame.font.SysFont("arialblack",20),(255,255,255),300, 110 + i * 200,self.screen)
            draw_text(vida_total+" / "+vida_actual,pygame.font.SysFont("arialblack",20),(255,255,255),300, 140 + i * 200,self.screen)
            if i == self.selected_option:                                                   
                 pygame.draw.rect(self.screen, (128, 128, 128), rect.inflate(10, 10))
            self.screen.blit(diseno_p,(450, 80 + i * 200))
            self.screen.blit(text, rect)

    def cambio_pokemon(self,Pokemones: dict,opc,identi):
        running=True
        if opc==1:
            id=1
        elif opc==2:
            id=4
        while running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir(self.screen)
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif evento.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif evento.key==pygame.K_BACKSPACE:
                        return 0
                    elif evento.key == pygame.K_RETURN:
                        selected_action = self.options[self.selected_option]
                        if selected_action == "Pokemon 1":
                            if Pokemones[id].get_vida_actual()<=0:
                                print("No tiene la suficiente vida para pelear")
                            elif identi==id:
                                print("Escoga otro pokemon")
                            else:
                                return id
                        elif selected_action=="Pokemon 2":
                            id=id+1
                            if Pokemones[id].get_vida_actual()<=0:
                                print("No tiene la suficiente vida para pelear")
                                id=id-1
                            elif identi==id:
                                print("Escoga otro pokemon")
                                id=id-1
                            else:
                                return id
                        elif selected_action=="Pokemon 3":
                            id=id+2
                            if Pokemones[id].get_vida_actual()<=0:
                                print("No tiene la suficiente vida para pelear")
                                id=id-2
                            elif identi==id:
                                print("Escoga otro pokemon")
                                id=id-2
                            else:
                                return id
            self.screen.blit(self.fondo,(0,0))
            if opc==1:
                self.draw_menu(Pokemones,id)
            elif opc==2:
                self.draw_menu(Pokemones,id)
            pygame.display.flip()

def draw_text(text,Press,Color_texto,x,y,fondu):
    img=Press.render(text,True,Color_texto)
    fondu.blit(img,(x,y))

def salir(screen):
    fondo=(0,0,0)
    running=True
    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running=False
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    running=False
                elif evento.key==pygame.K_BACKSPACE:
                    sys.exit()
            screen.fill(fondo)
            draw_text("Esta seguro que quiere salirse?",pygame.font.SysFont("arialblack",20),(255,255,255),500,200,screen)
            draw_text("Enter: No    BackSpace: Si",pygame.font.SysFont("arialblack",20),(255,255,255),500,300,screen)
            pygame.display.flip()

def victoria(screen,mensaje):
    fondo_victoria=pygame.image.load("Sprites\Victoria.jpg")
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Sonidos\Victoria_Sonido.mp3")
    pygame.mixer.music.play(-1)
    running=True
    while running:
        for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir(screen)
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        Desarrollo1.main()
        screen.blit(fondo_victoria,(0,0))
        draw_text(mensaje,pygame.font.SysFont("arialblack",50),(0,0,0),300,300,screen)
        draw_text("Quieres hacer otra pelea? Presiona Enter",pygame.font.SysFont("arialblack",40),(0,0,0),100,500,screen)
        pygame.display.flip()