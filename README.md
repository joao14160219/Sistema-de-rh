🧩 HRManager
----

Sistema de apoio à gestão de Recursos Humanos com foco em visualização, controle e automação de dados.

📌 Visão Geral
-

O HRManager é um sistema desktop integrado a uma API backend, desenvolvido para centralizar informações de colaboradores, facilitar consultas rápidas e oferecer indicadores visuais de RH, reduzindo a dependência de planilhas e processos manuais.

O projeto nasceu como um desafio técnico e funcional, com foco em arquitetura, integração e boas práticas de desenvolvimento.

🎯 Objetivo do Sistema
-

Centralizar dados de colaboradores

Facilitar consultas e cadastros

Oferecer dashboards com KPIs de RH

Controlar acesso por perfil de usuário

Servir como base para automações futuras

O sistema não substitui ERPs corporativos, mas atua como uma camada de apoio e visualização.

🏗️ Arquitetura
-

O HRManager utiliza uma arquitetura desktop + API, separando claramente responsabilidades.

[ Desktop (PySide6) ]

        ↓  HTTP (JSON)
        
[ API FastAPI ]

        ↓
        
[ SQLite Database ]


📌 Camadas 
-

Frontend Desktop: Interface gráfica para usuários finais

Backend API: Regras de negócio, segurança e acesso a dados

Banco de Dados: Persistência das informações

🖥️ Interface Desktop 
-
Desenvolvida em PySide6 (Qt), com foco em usabilidade e organização visual.

Funcionalidades:

Tela de login

Dashboard com indicadores

Cadastro e edição de funcionários

Listagem e consulta rápida

Gestão de usuários (acesso restrito)

🔐 Segurança e Controle de Acesso
Autenticação
-

Login via API

Retorno de token de sessão

Token enviado no header X-Token em todas as requisições

Senhas

Senhas armazenadas com hash seguro (PBKDF2)

Nenhuma senha é salva em texto puro

Perfis de usuário

Controle de permissões por role

Exemplo:

Usuário comum: visualização

Admin: gestão de funcionários

Host: acesso total (usuários + dados)

📊 Dashboard e Indicadores
-

O sistema apresenta KPIs calculados no backend e exibidos no desktop:

Total de funcionários

Massa salarial

Salário médio

Distribuição por departamento

Distribuição por estado

Gráficos

Gráficos de pizza e barras

Renderizados com Matplotlib

Integrados diretamente à interface Qt

🗂️ Funcionalidades Principais
-
👤 Funcionários
-

Cadastro

Edição

Exclusão

Consulta por lista

Visualização detalhada

👥 Usuários
-

Criação de usuários

Definição de perfil

Exclusão

Controle de acesso por permissão

🛠️ Tecnologias Utilizadas
-

Python

FastAPI (backend)

SQLite (banco de dados)

PySide6 (Qt) (desktop)

Matplotlib (gráficos)

SQLAlchemy (ORM)

Requests (comunicação API)

🔒 Boas Práticas Adotadas
-

Separação clara entre frontend e backend

Uso de API para todas as operações

Hash seguro de senhas

Controle de sessão por token

Código modular e organizado

Validações no frontend e backend

⚠️ Limitações Conhecidas
-

Banco de dados local (SQLite)

Ambiente local (sem deploy distribuído)

Não substitui sistemas ERP completos

Projeto em evolução

Essas limitações são intencionais, dado o escopo e objetivo do projeto.

🚀 Possíveis Evoluções
-

Migração para banco de dados corporativo (PostgreSQL)

Logs e auditoria

Integração com sistemas externos

Relatórios avançados

Controle mais granular de permissões

Deploy em ambiente corporativo

🧪 Status do Projeto
-

🟡 Projeto em desenvolvimento / estudo técnico
