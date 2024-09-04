FROM node:22.8.0-bookworm AS build

WORKDIR /app

COPY package.json .
COPY package-lock.json .

RUN npm i

COPY src/ src/
COPY public/ public/
COPY tsconfig.json .
COPY .env .

RUN node -r dotenv && npm run build

FROM nginx AS prod

COPY ops/nginx.conf /etc/nginx/nginx.conf

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 8080

# Запускаем nginx
CMD ["nginx", "-g", "daemon off;"]
