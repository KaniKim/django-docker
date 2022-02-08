FROM node:lts-alpine

ADD package.json ./
RUN npm install 

ADD . ./
RUN npm run build
CMD ["npm", "run", "serve"]