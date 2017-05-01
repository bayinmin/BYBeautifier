import os, json,sys

def get_file_content(filename, kbase_dir):
    if not os.path.isabs(filename):
        filename = os.path.join(kbase_dir,filename)
    try:
        with open(filename) as data_file:
            data = json.load(data_file)
        return data
    except:
        print "Unable to read the file"
        sys.exit(1)

def write_json_output_file(content, filename, base_dir):
    output_file = generate_default_filename(filename)
    with open(output_file, 'w') as out_f:
        out_f.write(content)

def generate_default_filename(filename):
    base_name = os.path.basename(filename)
    return "pretty-" + base_name