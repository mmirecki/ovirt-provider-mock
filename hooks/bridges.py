import subprocess

def run(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    if process.wait() != 0:
        raise Exception(process.stderr.read())
    output = process.stdout.read()
    return output


def add_bridge(bridge_name):
    run(['/sbin/brctl', 'addbr', bridge_name])

def does_bridge_exist(bridge_name):
    return bridge_name in get_all_bridges()

def get_all_bridges():
    process_output = run(['brctl', 'show'])
    output_lines = process_output.splitlines()[1:]
    tokenized_lines = map(str.split, output_lines)
    bridge_lines = filter(lambda bridge_tokens: len(bridge_tokens) > 1, tokenized_lines)
    bridge_names = map(lambda tokens: tokens[0], bridge_lines)
    return bridge_names

