import tools

### FUNCIONES ###

# Funcion simple
def hello():
    print("Hello")


# Invoco a la funcion
hello()


# Funcion con parametros o argumentos (es lo mismo)
def bye(user):
    print(f"Bye bye {user.title()}")


bye("Antonio")


# Argumentos de palabra clave
def full_name(first_name, last_name):
    print(f"First name -> {first_name}")
    print(f"Last name -> {last_name}")


full_name(first_name='Antonio', last_name='Ruiz')


# Valores predeterminados en funciones

def describe_pet(pet_name, animal_type="dog"):
    print(f"Type animal {animal_type}")
    print(f"Name: {pet_name}")


describe_pet(pet_name="chula")
describe_pet('nala')
describe_pet('momo', 'snake')


# Camiseta
def make_shirt(size, message):
    print(f"{size} {message}")


make_shirt(38, 'Your size is')
make_shirt(size=29, message='Your size is')


def make_t_shirt(size='XL', message='I love Python'):
    print(f"{size} {message}")


make_t_shirt()  # Funcion con valores predeterminados
make_t_shirt('S')  # Funcion con el parametro mensaje predeterminado
make_t_shirt('M', 'Hello Word')  # Funcion con parametros distintos a los predeterminados


# Ciudades
def describe_city(city, country='Spain'):
    print(f"{city} is in {country}.")


describe_city('Madrid')
describe_city('Paris', 'France')


### FUNCIONES CON RETORNO ###
def dog_owner(owner_name, dog_name):
    information = f"Owner: {owner_name} || Dog: {dog_name}"  # Variable que contiene la informacion y sera retornada
    return information.title()  # Retornamos la variable


owner_one = dog_owner('antonio', 'chula')  # Utilizando la funcion asignamos los parametros introducidos en la variable
print(owner_one)  # Imprimimos la variable


# Crear un parametro opcional dentro de una funcion
def get_formated_informatio(first_name, last_name,
                            age=''):  # Para convertir la variable 'age' en opcional asignamos un valor predeterminado vacio para ignorarlo a menos que se desee lo contrario
    if age:  # Comprobamos si la variable 'age' esta vacia, de no ser asi
        full_information = f'{first_name} {last_name} {age}'
    else:
        full_information = f'{first_name} {last_name}'

    return full_information.title()


information = get_formated_informatio('antonio', 'ruiz', 35)  # Ejemplo con todos los parametros
print(information)

information_2 = get_formated_informatio('arya', 'ruiz')  # Ejemplo ignorando la variable 'age'
print(information_2)


### Funcion para retornar un diccionario
def employe_information(id, first_name):
    employe = {'id_employe': id,
               'first_name': first_name}  # Asigno a la variable las claves y valores para poder retornarlos

    return employe


dictionary_employes = employe_information('03', 'antonio')
print(dictionary_employes)


def dictionary_employes(id, first_name,
                        age=None):  # Asigno una variable opcional llamada 'age' sin valor indicandolo con la palabra clave None
    employe = {'id_employe': id, 'first_name': first_name}  # Creo el diccionario

    if age:  # Si el parametro age tiene un valor se lo asignamos en el diccionario
        employe['age'] = age

    return employe  # Retornamos la variable con la informacion


employes = dictionary_employes('69', 'Patricia')  # Ignoramos el parametro age
print(employes)

employes_2 = dictionary_employes('33', 'Chula', 9)  # Incluimos el parametro age
print(employes_2)


# Funcion con bucle while
def new_employe(id, name):
    full_information = f"{id} : {name}"
    return full_information.title()


while True:
    print('Hello!!! if you want to exit press 0.')
    print("Enter your id:")
    id = input('Id:')

    print('Enter your name: ')
    name = input('Name: ')
    # Si alguno de los valores de la variable es 0 el programa terminara utilizando la palabra clave break
    if id == '0':
        break

    if name == '0':
        break

new_employe = new_employe(id, name)


# Nombres de ciudad
def name_city(city, country):
    new_city = f'{city}, {country}'

    return new_city.title()


new_city_1 = name_city('madrid', 'spain')
new_city_2 = name_city('roma', 'italy')
new_city_3 = name_city('valencia', 'Spain')

print(new_city_1)
print(new_city_2)
print(new_city_3)


# Album
def make_album(artist, album):
    album_information = {'Artist': artist, 'Album': album}

    return album_information


artist_1 = make_album('Eminem', 'The real slim shady')
artist_2 = make_album('Dr Dre', 'Dr Dre 2001')
artist_3 = make_album('Tupac', '2 pac')

print(artist_1)
print(artist_2)
print(artist_3)


def make_album(artist, album, number_of_songs=None):
    album_information = {'Artist': artist, 'Album': album}

    if number_of_songs:
        album_information['Number of Songs'] = number_of_songs

    return album_information


artist_4 = make_album('Ice Cube', 'Ice', '19')
print(artist_4)

control = True # Variable para controlar el bucle
album_list = [] # Creo un diccionario vacio para poder guardar la informacion que introduzca el usuario

while control:
    print('Indicates the name of the artist:') # Pido el valor
    name = input('Name: ') # Guardo el valor

    print('Indicates the name of the album:')
    album_name = input('Album: ')

    print('Indicates number of songs:')
    songs = input('Songs: ')

    print('If you want to continue press [s] otherwise press [n]:') # Pregunto si desea seguir introduciendo informacion
    decision = input() # Guardo el valor

    informations = make_album(name, album_name, songs)
    album_list.append(informations) # Agrego la nueva informacion al diccionario

    if decision.lower() == 'n': # Compruebo si el usuario desea salir
        print('Bye bye....')
        control = False # Cambio la variable a False para salir del bucle

for album in album_list:
    print(album)

### Pasar una lista como parametro a una funcion

original_list = ['a', 'b', 'c', 'd'] # Lista orignal
new_list = [] # Lista vacia donde introducire los elementos de la lista original

### Metodo para mover elementos de una lista a otra ###
def move_from_one_list_to_another(original_list, new_list):
    while original_list:
        origin = original_list.pop() # Obtenemos el elemento y lo eliminamos de la lista original empezando por el final
        print('adding item to new list')

        new_list.append(origin) # Añadimos el elemento a la nueva lista

### Metodo para imprimir todos los elementos de una lista ###
def scroll_list_and_print(new_list):
    for element in new_list:
        print(element)

move_from_one_list_to_another(original_list, new_list)
scroll_list_and_print(new_list)
print(f"Original List -> {original_list}") # La lista original ya no contiene elementos

### Evitar que un metodo modifique una lista
# nombre_del_metodo([:]) utilizando la notacion [:] se genera una copia de la lista original, para no modificar ni trabajar con la lista original
move_from_one_list_to_another(original_list[:], new_list) # De esta forma la lista original_list no se vera afectada por ningun cambio

# Mostrar Mensajes
messages_list = ["hello world", "Hi woman", "Bye man"]
def show_message(message_list):
    for message in message_list:
        print(message)

show_message(messages_list)


# Enviar mensajes

def send_message(message_list, message_sent):
    while message_list:
        message = message_list.pop()

        print("Sending message...")

        message_sent.append(message)

messages_send = []

send_message(messages_list, messages_send)

print(messages_list)
print(messages_send)

# Utilizar una copia de mensages_send para no modificar la lista original

new_send_messages = []

send_message(messages_send[:], new_send_messages) # En el primer parametro paso una copia de la lista indicandolo con [:] para que no sea modificada

print(messages_send)
print(new_send_messages)

### Crear un metodo que reciba un numero de parametros indeterminados  utilizando '*' ###
def method_with_undetermined_parameters(*indeterminate_parameters):
    print(indeterminate_parameters)

method_with_undetermined_parameters(1,2,3,4)
method_with_undetermined_parameters('Arya', 'Patricia')
method_with_undetermined_parameters('chula', 98)

### Crear un metodo que reciba parametros posicionales y un numero indeterminado de parametros
# Hay que poner el numero undeterminado de parametros al final de los parametros
def parameters_determined_indeterminate(parameter_1, parameter_2, *undeterminate_parameters):
    print(f"{parameter_1} {parameter_2}") # Imprimo los parametros determinados

    for parameter in undeterminate_parameters: # Recorro e imprimo los parametros indeterminados que iran en la tupla "undeterminate_parameters"
        print(parameter)


parameters_determined_indeterminate(1, 'Hi', 1,2,3, 'Bye')

### Crear un metodo utilizando un diccionario de claves valor indeterminado utlizando '**'
def employee_profile(id, name, **employee_info): # Utilizando ** hace que python cree un diccionario vacio
    employee_info['ID'] = id # Clave - Valor
    #           Clave  = Valor
    employee_info[name] = name

    return employee_info

# Utilizando el metodo creo un diccionario que podra admitir un numero indeterminado de claves - valores
employee_info = employee_profile( 1, 'Antonio',
                                 city = 'Madrid',
                                  country = 'Spain')

print(employee_info)

### Llamada a una funcion dentro de un modulo, habiendo echo previamente el import correspondiente
# LLamamos al modulo correspondiente y al metodo
tools.greeting()