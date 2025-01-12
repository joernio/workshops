from flask import Flask, request, jsonify
import os
import subprocess
import sys

class FileLister:
    def __init__(self):
        self.app = Flask(__name__)

    def list_files_directory(self):
        @self.app.route('/list-files-directory', methods=['GET'])
        def get_list_files_directory():
            directory = request.args.get('directory')
            if not os.path.isdir(directory):
                return jsonify({'error': 'Invalid directory'}), 400
            try:
                output = subprocess.check_output(["ls", "-1", directory]).decode("utf-8")
                return jsonify([os.path.join(directory, line) for line in output.splitlines()])
            except subprocess.CalledProcessError as e:
                return jsonify({'error': str(e)}), 500

    def list_files_directory_os_walk(self):
        @self.app.route('/list-files-directory-os-walk', methods=['GET'])
        def get_list_files_directory_os_walk():
            directory = request.args.get('directory')
            if not os.path.isdir(directory):
                return jsonify({'error': 'Invalid directory'}), 400
            try:
                return jsonify([os.path.join(root, name) for root, dirs, files in os.walk(directory)
                                for name in files])
            except Exception as e:
                return jsonify({'error': str(e)}), 500

    def list_files_directory_os_listdir(self):
        @self.app.route('/list-files-directory-os-listdir', methods=['GET'])
        def get_list_files_directory_os_listdir():
            directory = request.args.get('directory')
            if not os.path.isdir(directory):
                return jsonify({'error': 'Invalid directory'}), 400
            try:
                return jsonify([os.path.join(directory, name) for name in os.listdir(directory)
                                if os.path.isfile(os.path.join(directory, name))])
            except Exception as e:
                return jsonify({'error': str(e)}), 500

    def list_files_directory_popen(self):
        @self.app.route('/list-files-directory-popen', methods=['GET'])
        def get_list_files_directory_popen():
            directory = request.args.get('directory')
            if not os.path.isdir(directory):
                return jsonify({'error': 'Invalid directory'}), 400
            try:
                output = []
                with subprocess.Popen(["ls", "-1", directory], stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT, bufsize=1) as p:
                    for line in p.stdout:
                        output.append(os.path.join(directory, line.decode("utf-8").strip()))
                return jsonify(output)
            except Exception as e:
                return jsonify({'error': str(e)}), 500

    def list_files_directory_popen_shell(self):
        @self.app.route('/list-files-directory-popen-shell', methods=['GET'])
        def get_list_files_directory_popen_shell():
            directory = request.args.get('directory')
            if not os.path.isdir(directory):
                return jsonify({'error': 'Invalid directory'}), 400
            try:
                output = subprocess.check_output(["ls", "-1", directory], shell=True).decode("utf-8")
                return jsonify([os.path.join(directory, line) for line in output.splitlines()])
            except Exception as e:
                return jsonify({'error': str(e)}), 500

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    app = FileLister()
    app.list_files_directory()
    app.list_files_directory_os_walk()
    app.list_files_directory_os_listdir()
    app.list_files_directory_popen()
    app.list_files_directory_popen_shell()
    app.run()
