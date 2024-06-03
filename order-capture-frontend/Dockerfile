# Use Node.js as base image
FROM node:14 AS build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json yarn.lock ./

# Install dependencies
RUN yarn install --frozen-lockfile

# Copy the entire project
COPY . .

# Build the Vue.js application
RUN yarn build

# Use nginx as base image for serving static files
FROM nginx:alpine

# Copy built files from the previous stage to nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80
# EXPOSE 8000

# Start nginx server
CMD ["nginx", "-g", "daemon off;"]
