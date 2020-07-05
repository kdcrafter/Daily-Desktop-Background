import xml.etree.ElementTree as ET
import shutil
import sys
import os

TASK_NAMESPACE = 'http://schemas.microsoft.com/windows/2004/02/mit/task'
TASK_XML_FILENAME = 'Daily-Desktop-Background.xml'

def update_xml():
    ns = {'windows_task': TASK_NAMESPACE}

    tree = ET.parse(TASK_XML_FILENAME)
    root = tree.getroot()

    actions = root.find('windows_task:Actions', ns)

    exec = actions[0]
    command = exec.find('windows_task:Command', ns)
    command.text = sys.executable
    woring_dir = exec.find('windows_task:WorkingDirectory', ns)
    woring_dir.text = os.getcwd()

    exec = actions[1]
    command = exec.find('windows_task:Command', ns)
    command.text = shutil.which('powershell')
    woring_dir = exec.find('windows_task:WorkingDirectory', ns)
    woring_dir.text = os.getcwd()

    tree.write(TASK_XML_FILENAME, encoding="utf-16", xml_declaration=True)

if __name__ == '__main__':
    ET.register_namespace('', TASK_NAMESPACE)
    update_xml()