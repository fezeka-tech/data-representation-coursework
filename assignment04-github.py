import os
import git

def replace_text_in_file(file_path, old_text, new_text):
    with open(file_path, 'r') as file:
        content = file.read()
        content = content.replace(old_text, new_text)

    with open(file_path, 'w') as file:
        file.write(content)

def commit_and_push_changes(repo, file_path, commit_message):
    repo.index.add([file_path])
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push()

def main():
    repo_path = 'https://github.com/fezeka-tech/data-representation-coursework.git'
    file_name = 'Name.txt'
    old_text = 'Andrew'
    new_text = 'Fezeka'
    commit_message = 'Replace "Andrew" with "Fezeka"'

    file_path = os.path.join(repo_path, file_name)

    # Open the Git repository
    repo = git.Repo(repo_path)

    # Replace text in the file
    replace_text_in_file(file_path, old_text, new_text)

    # Commit and push changes
    commit_and_push_changes(repo, file_path, commit_message)

if __name__ == '__main__':
    main()
