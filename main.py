import os
import time
import git

repo_path = r'C:\Users\Nicolas\Desktop\finvivir'  # Cambia esto a la ruta de tu repositorio local


def auto_commit():
    repo = git.Repo(repo_path)

    while True:
        status = repo.git.status()

        if "Changes not staged for commit" in status or "Untracked files" in status:
            repo.git.add('--all')
            commit_message = f'AutoSave {time.strftime("%d/%m/%Y")} #{len(repo.head.log()) + 1}'
            repo.git.commit('-m', commit_message)
            print(f'Committed: {commit_message}')
            repo.remotes.origin.push()
            print('Pushed changes.')
        else:
            print('No changes to commit.')

        time.sleep(300)  # Espera 5 minutos (300 segundos)


if __name__ == '__main__':
    if os.path.exists(repo_path):
        auto_commit()
    else:
        print("Ruta de repositorio inválida.")
