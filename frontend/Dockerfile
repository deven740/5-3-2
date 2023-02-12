FROM node:alpine
WORKDIR /home/node
COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . .
CMD npm start