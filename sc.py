import os

def create_folders_and_files(folder_name, location):
    # Tworzenie głównego folderu o podanej nazwie w danej lokalizacji
    folder_path = os.path.join(location, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Tworzenie folderu "client" w głównym folderze
    client_folder = os.path.join(folder_path, "client")
    os.makedirs(client_folder, exist_ok=True)

    # Tworzenie pliku "client.lua" w folderze "client"
    client_lua_path = os.path.join(client_folder, "client.lua")
    with open(client_lua_path, "w") as client_lua_file:
        client_lua_file.write("ESX = exports.es_extended.getSharedObject()")

    # Tworzenie folderu "server" w głównym folderze
    server_folder = os.path.join(folder_path, "server")
    os.makedirs(server_folder, exist_ok=True)

    # Tworzenie pliku "server.lua" w folderze "server"
    server_lua_path = os.path.join(server_folder, "server.lua")
    with open(server_lua_path, "w") as server_lua_file:
        server_lua_file.write("ESX = exports.es_extended.getSharedObject()")

    # Tworzenie pliku "config.lua" w głównym folderze
    config_lua_path = os.path.join(folder_path, "config.lua")
    with open(config_lua_path, "w") as config_lua_file:
        config_lua_file.write("Config = {}")

    # Tworzenie pliku "fxmanifest.lua" w głównym folderze
    fxmanifest_lua_path = os.path.join(folder_path, "fxmanifest.lua")
    with open(fxmanifest_lua_path, "w") as fxmanifest_lua_file:
        fxmanifest_lua_file.write(f"""fx_version 'cerulean'
game 'gta5'

author 'Sernikov'

shared_script 'config.lua'

client_script 'client/client.lua'
server_script 'server/server.lua'
""")

if __name__ == "__main__":
    folder_name = input("Podaj nazwę folderu: ")
    location = input("Podaj lokalizację, w której chcesz utworzyć folder i pliki: ")
    create_folders_and_files(folder_name, location)
    print("Struktura folderu i plików została utworzona.")
