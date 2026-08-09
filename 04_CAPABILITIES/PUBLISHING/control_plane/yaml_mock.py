"""
Minimal YAML mock for testing when PyYAML is unavailable.
Only supports the specific YAML patterns used by the destination registry.
"""

import json
import re
from typing import Any, Dict


def safe_load(file_obj) -> Dict[str, Any]:
    """
    Minimal YAML parser that handles destination registry YAML.
    Parses only the specific patterns we use.
    """
    content = file_obj.read()
    if isinstance(content, bytes):
        content = content.decode('utf-8')

    # Simple state machine for parsing the minimal YAML we use
    result = {}
    current_section = None
    current_list = None
    current_obj = None
    stack = []

    for line in content.split('\n'):
        # Strip line
        line = line.rstrip()

        # Skip empty lines and comments
        if not line.strip() or line.strip().startswith('#'):
            continue

        # Calculate indentation
        indent = len(line) - len(line.lstrip())
        stripped = line.lstrip()

        # Schema version
        if ':' in stripped and not stripped.startswith('['):
            key, val = stripped.split(':', 1)
            key = key.strip()
            val = val.strip()

            if indent == 0:
                # Top level
                if val.startswith('"') and val.endswith('"'):
                    result[key] = json.loads(val)
                else:
                    result[key] = val
            elif indent == 2 and current_list is not None:
                # Property of list item
                if val.startswith('"') and val.endswith('"'):
                    current_obj[key] = json.loads(val)
                elif val.lower() == 'true':
                    current_obj[key] = True
                elif val.lower() == 'false':
                    current_obj[key] = False
                else:
                    current_obj[key] = val
            elif indent == 4 and current_obj is not None and 'auth' in current_obj:
                # auth properties
                if current_obj.get('_in_auth'):
                    if val.startswith('['):
                        # Parse list
                        items = []
                        current_obj['secret_refs'] = items
                    else:
                        if key == 'method':
                            current_obj['auth']['method'] = val
        elif stripped.startswith('- '):
            # List item
            if current_section == 'destinations':
                if current_obj:
                    if 'destinations' not in result:
                        result['destinations'] = []
                    result['destinations'].append(current_obj)
                current_obj = {}
                current_list = result.get('destinations', [])

        elif stripped == 'destinations:':
            current_section = 'destinations'
            if 'destinations' not in result:
                result['destinations'] = []
            current_list = result['destinations']
        elif stripped == 'auth:':
            if current_obj is not None:
                current_obj['auth'] = {}
                current_obj['_in_auth'] = True
        elif ':' in stripped and indent >= 4:
            # Nested properties
            key, val = stripped.split(':', 1)
            key = key.strip()
            val = val.strip()

            if current_obj is not None:
                if 'auth' in current_obj and indent == 6:
                    if val.startswith('['):
                        current_obj['auth']['secret_refs'] = []
                    else:
                        if key == 'method':
                            current_obj['auth'][key] = val
                elif indent == 6 and key == 'secret_refs':
                    if val.startswith('-'):
                        current_obj['auth']['secret_refs'] = []
                elif indent == 8 and 'secret_refs' in current_obj.get('auth', {}):
                    if stripped.startswith('- '):
                        current_obj['auth']['secret_refs'].append(stripped[2:].strip().strip('"'))
                elif current_obj and 'auth' not in current_obj:
                    if val.startswith('"') and val.endswith('"'):
                        current_obj[key] = json.loads(val)
                    elif val.lower() == 'true':
                        current_obj[key] = True
                    elif val.lower() == 'false':
                        current_obj[key] = False
                    else:
                        current_obj[key] = val
                elif current_obj and 'auth' in current_obj and indent >= 6:
                    if key not in current_obj['auth']:
                        current_obj['auth'][key] = []
                    if isinstance(val, str) and val.startswith('- '):
                        current_obj['auth'][key].append(val[2:].strip().strip('"'))
                    elif val:
                        if isinstance(current_obj['auth'][key], list):
                            current_obj['auth'][key].append(val.strip('"'))
                        else:
                            current_obj['auth'][key] = val.strip('"')
        elif indent == 8 and stripped.startswith('- ') and current_obj is not None:
            # Secret refs list item
            if 'auth' in current_obj:
                val = stripped[2:].strip().strip('"')
                if 'secret_refs' not in current_obj['auth']:
                    current_obj['auth']['secret_refs'] = []
                current_obj['auth']['secret_refs'].append(val)

    # Add last object if exists
    if current_obj and 'destination_id' in current_obj:
        if 'destinations' not in result:
            result['destinations'] = []
        result['destinations'].append(current_obj)

    return result
