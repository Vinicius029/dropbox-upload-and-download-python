import dropbox.files
import dropbox
import os
import hashlib

with open ("token.txt", "r") as f:
    token = f.read()


dbx = dropbox.Dropbox(token)


def dropbox_content_hash(file):
    hash_size = 4 * 1024 * 1024
    with open(file, 'rb') as f:
        block_hashes = bytes()
        while True:
            chunk = f.read(hash_size)
            if not chunk:
                break
            block_hashes += hashlib.sha256(chunk).digest()
        return hashlib.sha256(block_hashes).hexdigest()
    
def download_changed():
    try:
        for entry in dbx.files_list_folder('').entries:
            if os.path.exists(os.path.join('local_files', entry.name)):
                local_hash = dropbox_content_hash(os.path.join('local_files', entry.name))
                if local_hash != entry.content_hash:
                    print(f'Arquivo alterado: {entry.name}')
                    dbx.files_download_to_file(os.path.join('local_files', entry.name), f'/{entry.name}')
                else:
                    print(f'Arquivo Inalteraedo: {entry.name}')
            else:
                print(f"Novo Arquivo: {entry.name}")
                dbx.files_download_to_file(os.path.join('local_files', entry.name), f"/{entry.name}")
        os.system('pause')
    except Exception:
        print(Exception)
    


def upload_changed():
    try:
        cloud_files = {e.name: e.content_hash for e in dbx.files_list_folder('').entries}
        for file in os.listdir('local_files'):
            if file in cloud_files.keys():
                local_hash = dropbox_content_hash(os.path.join('local_files', file))
                if local_hash != cloud_files[file]:
                    print(f'Arquivo alterado: {file}')
                    with open(os.path.join('local_files', file), 'rb') as f:
                        data = f.read()
                        dbx.files_upload(data, f'/{file}', mode=dropbox.files.WriteMode('overwrite'))
                else:
                    print(f'Arquivo Inalteraedo: {file}')
            else:
                print(f'Arquivo Novo: {file}')
                with open(os.path.join('local_files', file), 'rb') as f:
                    data = f.read()
                    dbx.files_upload(data, f'/{file}', mode=dropbox.files.WriteMode('overwrite'))
        os.system('pause')
    except Exception:
        print(Exception)
    


while True:
    os.system('cls')
    opc = int(input('ESCOLHA UMA DAS OPÇÃO:\n[1] - Upload\n[2] - Download\n[0] - Fechar programa\n'))
    if opc == 1:
        upload_changed()
    elif opc == 2:
        download_changed()
    else:
        break
    
