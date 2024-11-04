PYTHON = python3
PIP = pip3

# Instalando as dependências
install:
	$(PIP) install -r requirements.txt

# Executando o código principal
run:
	$(PYTHON) main.py

# Limpando os arquivos temporários
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.db" -exec rm -rf {} +

# Realiza uma query
query:
	$(PYTHON) query.py

# Inserir dados na agenda
insert:
	$(PYTHON) insert.py

# Listando os comandos existentes
help:
	@echo "Comandos disponíveis:"
	@echo "	make install		:	Instala as dependências do projeto;"
	@echo "	make run		:	Executa o código principal do projeto;"
	@echo "	make clean		:	Remove os arquivos temporários;"
	@echo "	make query		:	Realiza uma query;"
	@echo "	make insert		:	Inserir dados no banco;"
	@echo "	make help		:	Lista os comandos."