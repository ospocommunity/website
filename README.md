# OSPO Summit hugo site

This repository contains a Hugo based site for OSPO Summit.

NOTE: Please use hugo v0.92.2 to avoid the website build error.

To install Hugo :

```
brew install hugo
# or
port install hugo
```

Please chose hugo below v0.93, otherwise the build will failed.  

To test it locally, run:

```
hugo server -b http://localhost:1313 -F
```

To generate final site, use:


```
hugo -b https://apachecon.com/ -d <destination_directory> -F
```

