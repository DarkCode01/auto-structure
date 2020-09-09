## Simple script to create auto structure projects using yaml

#### Example:

1) Yaml file of structur project:

```yaml
# pattern.yml
- dir:
  contents:
    - dir:
      name: services
      contents:
        - file:
          prefix: "-"
          ext: services.module.js
        - file:
          prefix: "-"
          ext: services.service.js
    - file:
      ext: component.js
    - file:
      ext: module.js
    - file:
      ext: scss
    - file:
      ext: tmpl.html
```

2) entry on project and run it

```bash
~$ cd ~/auto-structure
~$ python3 auto.py location-status-editor ../test ../pattern.yml
* location-status-editor (✅)
| -- * services (✅)
| -- location-status-editor-services.module.js (✅)
| -- location-status-editor-services.service.js (✅)
| -- location-status-editor.component.js (✅)
| -- location-status-editor.module.js (✅)
| -- location-status-editor.scss (✅)
| -- location-status-editor.tmpl.html (✅)
```

3) result:
```bash
~$ tree test/
test
└── location-status-editor
    ├── location-status-editor.component.js
    ├── location-status-editor.module.js
    ├── location-status-editor.scss
    ├── location-status-editor.tmpl.html
    └── services
        ├── location-status-editor-services.module.js
        └── location-status-editor-services.service.js
└── patter.yml
2 directories, 6 files
```
