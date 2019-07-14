import sys
import os
import requests
import argparse
import json

# quay.io API endpoint
quayio_endpoint = os.getenv("QUAYIO_ENDPOINT", "https://quay.io/api/v1/repository")

# get image manifest with specific tag from quay.io
def get_image_manifest(org, repo, tag):
    r = requests.get(quayio_endpoint + "/" + org + "/" + repo)
    image_manifest = ''
    if tag in r.json()['tags'].keys():
        image_manifest = r.json()['tags'][tag]['manifest_digest']
    return image_manifest

# retrieve image vulnerabilities information from quay.io
def scan_image_manifest(org, repo, manifest):
    r = requests.get(quayio_endpoint + "/" + org + "/" + repo + "/manifest/" + manifest + "/security?vulnerabilities=true")
    features = r.json()["data"]["Layer"]["Features"]
    vulnerabilities = []
    for item in features:
        if 'Vulnerabilities' in item.keys():
            package_name = item['Name']
            vuls = item['Vulnerabilities']
            # set packange_name in each Vulnerabilities section
            for n in vuls:
                n.update( { "PackageName": package_name } )
            vulnerabilities.extend(vuls)
    return vulnerabilities

# set output to json format
def output_json(org, repo, tag, manifest, vulnerabilities):
    ret_json = {}
    ret_json['Organisation'] = org
    ret_json['Repository'] = repo
    ret_json['Tag'] = tag
    ret_json['Manifest'] = manifest
    ret_json['Vulnerabilities'] = vulnerabilities
    return ret_json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    args = parser.parse_args()
    print("Receiving input from file/stdin ...")

    if args.input is None:
        parser.print_usage()
        sys.exit(1)
    else:
        input_src = args.input.read()
        print(input_src)
        src_json = json.loads(input_src)

    output = []
    for item in src_json:
        org = item.get('Organisation','')
        repo = item.get('Repository','')
        tag = item.get('Tag','')
        print("Retrieving manifest digest from {}/{}:{} ...".format(org, repo, tag))
        manifest = get_image_manifest(org, repo, tag)
        if manifest == '' :
            print("Error: tag - {} does not found in {}/{}".format(tag, org, repo))
        else:
            print("{}".format(manifest))
            vulnerabilities = scan_image_manifest(org, repo, manifest)
            output.append(output_json(org, repo, tag, manifest, vulnerabilities))

    print(json.dumps(output, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()

