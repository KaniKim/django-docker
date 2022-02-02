FROM node:lts-alpine
WORKDIR /vue_spa
COPY package*.json /vue_spa/

COPY /vue_spa /vue_spa/
RUN npm install
CMD ["npm", "start"]
