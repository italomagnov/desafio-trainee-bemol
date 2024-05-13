# Desafio Prático Trainee

---

## Instruções para rodar localmente

### 1 - Fazer um clone do repositório

```git
git clone https://github.com/italomagnov/desafio-trainee-bemol
```

### 2 - Criar um ambiente virtual

O projeto é executado com dependências instaladas em um ambiente virtual. Por favor, crie um antes de instalar.

Para criar um ambiente virtual execute, dentro da pasta dados, do repositório clonado:

``` python
python -m venv .venv
```

Isso criará uma pasta .venv no diretório raiz que conterá os arquivos de dependência.

Ou use seu fluxo de trabalho de gerenciamento de pacotes preferido. A parte importante é isolar as dependências em um ambiente virtual
ambiente.

### 3 - Ativar ambiente virtual

Para ativar o ambiente virtual execute:

- On Windows

``` sh
.\.venv\Scripts\activate.bat ou
.\.venv\Scripts\activate.ps1
```

- On Mac or Linux:

```sh
source . venv/bin/activate
```

### 4 - Instalar dependências

Para instalar dependências, execute:

```python
pip install -r requirements.txt
```

### 6 - Executando Streamlit

Agora que toda a configuração está concluída, para executar o streamlit, que é a forma escolhida para acessar visualizar o relatório na página web, execute no terminal dentro da pasta Dados, onde está localizado o arquivo app.py:

```python
streamlit run app.py
```

Agora o app criado com streamlit pode ser visualizado no navegador nos links:

```sh
Local URL: http://localhost:8501
Network URL: http://192.168.1.10:8501
```
