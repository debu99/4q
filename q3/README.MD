Scan docker image vulnerability with Quay.io API

### Install
```
pip3 install -r requirement.txt
```

### Usage
```
python3 q3.py repo_info.txt
```
or
```
python3 q3.py < repo_info.txt
```
or
```
python3 q3.py <<EOF
> [
>   {
>    "Organisation":"coreos",
>    "Repository":"hyperkube",
>    "Tag":"v1.10.4_coreos.0"
>   },
>   {
>    "Organisation":"coreos",
>    "Repository":"dnsmasq",
>    "Tag":"v0.5.0"
>   }
> ]
> EOF
```

