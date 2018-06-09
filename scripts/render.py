import os
import yaml
import summary


class Maker(object):
    def __init__(self):
        self.config_file = '../chemistry/meta.yml'
        self.magic_dict = self.load_config(self.config_file)
        self.output_dir = '../../gitbook/chemistry/'
        self.working_dir = os.getcwd()
        self.s = summary.Summary()

    def replace(self, s):
        for each in self.magic_dict:
            if each in s:
                s = s.replace(each, self.magic_dict[each])
            if 'equation' in s:
                s = s.replace('equation', '反应方程')

        return s

    def load_config(self, f):
        with open(f, 'r') as c:
            conf = yaml.load(c.read())
        return conf['predefine']

    def handle_line(self, s):
        s = self.replace(s)
        if s.startswith(' '):
            return s[2:]
        elif s == '\n':
            return s
        else:
            return f'```\n\n## {s}\n```yaml\n'

    def make_md(self, f):
        lines = self.read_file_lines(f)
        body = lines[4:]
        render_text = [self.handle_line(l) for l in body]
        render_text.append('```')
        # print(render_text[0])
        name = f.split('-')[-1].split('.')[0] + '.md'
        # print(name)
        with open(self.output_dir + name, 'w') as md:
            md.write(''.join(render_text).split('\n', 2)[-1])
        print(''.join(render_text))

    @staticmethod
    def read_file_lines(path_to_file):
        with open(path_to_file, 'r') as f:
            data = f.readlines()
        return data  # [l for l in data if l != '\n']

    def make_files(self, path_to_files):
        files = os.listdir(path_to_files)
        os.chdir(path_to_files)
        notebooks = sorted([file for file in files if file.endswith('yml')])
        for f in notebooks:
            # print(f)
            self.make_md(f)

    def make(self):

        self.make_files('../chemistry/chemistry')
        self.make_files('../chemistry/basic')
        self.make_summary()

    def make_summary(self):
        self.s.make()


if __name__ == '__main__':
    m = Maker()
    # m.make_md('../化学/basic/1-1-pure_substance&mixture.yml')
    m.make_files('../chemistry/chemistry')
