# Etapa 1: build
FROM node:20-alpine AS build

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Etapa 2: servidor nginx para servir os arquivos
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html

# Configurar para não cachear, opcional
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
