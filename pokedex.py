import requests
from watchdog.observers.winapi import CreateEvent
from flet_core.cupertino_icons import METRONOME
from flet_core.icons import CATCHING_POKEMON_ROUNDED, CATCHING_POKEMON
from markdown_it.common.normalize_url import normalizeLink
from pkg_resources._vendor.jaraco.functools import except_
def obtener_pokemon():
    nombre =input("🔎´ingresa el nombre del pokemon:")
    url = ff"https://pokeapi.co/api/v2/pokemon/{nombre}"
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    
    datos = respuesta.json()
    nombre_pokemon =datos ["name"].capitalize()
    altura =datos["height"] / 10
    peso =datos["height"] / 10
    numero_pokedex = datos["id"]
    
    tipos =[tipo["type]["mane"].capitalize() for tipo in datos["types"]]
    habilidades = [hab["ability"]]["name"].capitalize() for  hab in datos["abilities"]]
    
    print("\n📖 POKEDEX")
    print(f"🔢 numero: {numero_pokedex}")
    print(f"🐉 nombre: {nombre_pokemon}")
    print(F"📏 altura: {altura} mentros")
    print(f"⚖ peso: {peso} metros")
    print(f"🔥 tipo(s): {´,´.join(tipo)}")
    print(f"💡 habilidades:{´,´.join(habilidades)}")
    
    except resquets.exceptions.HTTPError:
        print("❌ pokemon no encontrado. intentqa nuevamente.")
    except requests.exceptions.requestException: 
        print("❌ Error de conexion con la API.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    
    
    obtener_pokemon()
    
    
    🔎 ingresa el nombre del pokemon: eevee 
     📖 POKEDEX
     🔢 numero: 133
     🐉 nombre: eevee 
     📏 altura:0.3 metros
     ⚖ peso:6.5 kg 
     🔥 tipo(s): normal 
     💡 habilidades: run-away,adaptability,anticipacion

    inport request 
    
def  obtener_pokemon():
    nombre = input("🔎 ingresa el nombre del pokemon: ").strip().lower()
    url = f"https://pokeap1.co/api/v2/pokemon/{nombre}"
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status() #lanza un error si la solitud falla 
        
        datos = respuesta.json()
        nombre_pokemon = datos["name"].capitalize()
        altura = datos["height"] / 10 #convertir a metros
        peso = datos["weight"] / 10 #convertir a kg
        numero_pokedex = datos["id"]
        
        tipos =["type"]["name"].capitalize() for tipo in datos["types"]
        habilidades = [hab["hability"]["name"].cápitalize() for hab in datos["bilities"]]
        
        print("\n📖 POKEDEX")
        print(f"🔢 numero:{numero_pokedex}")
        print(f"🐉 nombre:{nombre_pokemon}")
        print(f"📏 altura:{altura} metros")
        print(f"⚖ peso: {peso} kg")
        print(f"🔥 tipo(s): {´,´.join{(tipo)}")
        print(f"💡 habilidades: {´,´,join(habilidades)}")
        
    except requests.exceptions.HTTPError:
        print("❌ pokemon no encontrado. intenta nuevamente.")
    except requests.exceptions.requesException:
        print("❌ error de conexion con la API.")
    except exception as e:
        print(f"❌ error inesperado: {e}")
        
# llamar a la funcion para que el usuario ingrese un pokemon
obtener_pokemon()