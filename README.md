# Bot Telegram — Integrações e Pagamentos

> 🛠️ **Projeto aplicado** — protótipo de bot em Python para estudar integrações externas, pagamentos Pix, webhooks e persistência de dados.

Projeto experimental desenvolvido em 2023 utilizando a API do Telegram como interface para um fluxo automatizado que dependia de serviços externos.

O projeto acabou reunindo diferentes desafios técnicos em uma única aplicação: interação por bot, persistência local, integração com uma API externa, geração de cobranças Pix, QR Code, webhooks HTTPS e tentativa de implantação em VPS.

## O que foi desenvolvido

- Bot para Telegram utilizando Python;
- Cadastro e persistência de usuários com SQLite e SQLAlchemy;
- Menus e interações utilizando botões inline;
- Integração com uma API externa;
- Integração com a API Pix da Gerencianet;
- Geração de cobranças e QR Codes Pix;
- Protótipo de webhook em Flask;
- Configuração experimental de HTTPS com certificados;
- Tentativas de implantação da aplicação em servidor VPS.

## Tecnologias

- Python
- pyTelegramBotAPI
- Flask
- Flask-SQLAlchemy
- SQLite
- Requests
- API Pix / Gerencianet
- Webhooks
- HTTPS / TLS

## Status

📚 Projeto descontinuado.

O desenvolvimento não chegou a uma versão de produção. A etapa de implantação e configuração do ambiente em servidor acabou sendo um dos principais pontos de dificuldade e o projeto foi interrompido.

O código é mantido como registro de uma fase de aprendizado envolvendo integração entre múltiplos serviços, pagamentos, webhooks e infraestrutura.

## Segurança

Credenciais, certificados, chaves e dados utilizados durante o desenvolvimento foram removidos ou substituídos por valores fictícios antes da publicação deste repositório.
