FROM node:lts-alpine
WORKDIR /vue_spa

ADD package.json ./
ADD . ./
RUN npm install
CMD ["npm", "run", "serve"]
