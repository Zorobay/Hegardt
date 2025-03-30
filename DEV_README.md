## TODO

 - [ ] Language selector
 - [ ] Search
 - PersonView
   - [x] Locations
   - [x] Parents
   - [x] Siblings
   - [x] Occupations
   - [x] Notes
   - [x] References
  - [ ] Map
   - [ ] Show markers for Birth, Death, Burial
   - [ ] Find person by name
   - [ ] Filter by year (Birth, Death, Burial)
   - [ ] Click marker to go to person page
   - [ ] Go to map from person page by clicking on Birth-, Death- or Burial place.
  - [ ] Family Tree
   - [ ] Filter by name
   - [ ] Select how many pre and post generations to show
   - [ ] Toggle siblings

## Debuggery

### `<router-link>` changes url but does not render page

#### Problem

Clicking a `<router-link>` changes the url but does not render the new content. Example:

```html
<router-link class="stretched-link" :to="{name: 'person', params: {id: id}}">Link</router-link>
```

#### Solution

https://stackoverflow.com/questions/59088216/vue-router-link-changes-url-but-does-not-change-router-view-component

 > Just write key attribute in router-view:
 > `<router-view :key="$route.path"></router-view>`
 > 

### History is not working, gets 404

https://router.vuejs.org/guide/essentials/history-mode#nginx

## Run local build for production

Install a simple HTTP server with `npm install --global http-server`

From the `Hegardt/dist` directory, serve the website locally with command `http-server`.

## Hosting

### DNS

For some reason, DNS did not work through HostUp, but worked immediately through Digital Ocean. So, the DNS A-record is setup through: https://cloud.digitalocean.com/networking/domains

### Web server on NAS

Nginx is a clusetfuck of complexity, so the website is simply setup using Synology Web Station:

https://www.youtube.com/watch?v=jnpsNDdKpiI&ab_channel=RyderCragie

Synology Web Server will server files from the `/volume1/web` directory.

### Let's encrypt certificate

Setup on the NAS from Control Panel > Security > Certificate

Add new certificate with "Add" button and fill out info.

After the certificate is created, click "Settings" and make sure that the correct certificate is chosen for the web service.

## Nginx

Directory: `/usr/local/etc/nginx/` 

Check config: `sudo nginx -t`

Restart: `sudo systemctl restart nginx`

## Digital Ocean Setup

SSH: `ssh root@134.209.240.67`

1. Install NodeJS via NVM: https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-22-04#option-3-installing-node-using-the-node-version-manager
2. Install Nginx: https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-22-04
3. 
