### Usage
```
$ helm install example -f values.yaml.example
$ helm get values ingress-test-a
domain: cn.swatrider.com
hosts:
- name: foo
- name: bar

$ for i in foo bar;do curl -L $i.cn.swatrider.com;done
foo
bar
```


