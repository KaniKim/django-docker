FROM node:lts-alpine

ADD package.json ./
RUN npm install 

ADD . ./
RUN npm run build && rm -rf /var/lib/apt/lists/* 
CMD [ "npm", "run", "serve" ]