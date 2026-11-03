import re

with open('/tmp/edac-dkms/ie31200_edac.c', 'r') as f:
    content = f.read()

# 1. Replace edac_module.h with edac_mc.h
content = content.replace('#include "edac_module.h"', '#include "edac_mc.h"')

# 2. Add ADL_S_4 macro after ADL_S_3
content = content.replace(
    '#define PCI_DEVICE_ID_INTEL_IE31200_ADL_S_3\t0x4648\t/* 6P+4E, e.g. i5-12600K */',
    '#define PCI_DEVICE_ID_INTEL_IE31200_ADL_S_3\t0x4648\t/* 6P+4E, e.g. i5-12600K */\n#define PCI_DEVICE_ID_INTEL_IE31200_ADL_S_4\t0x4650\t/* 6P+0E, e.g. i5-12500 */'
)

# 3. Add pci_device_id entry after ADL_S_3
content = content.replace(
    '\t{ PCI_VDEVICE(INTEL, PCI_DEVICE_ID_INTEL_IE31200_ADL_S_3), (kernel_ulong_t)&rpl_s_cfg},',
    '\t{ PCI_VDEVICE(INTEL, PCI_DEVICE_ID_INTEL_IE31200_ADL_S_3), (kernel_ulong_t)&rpl_s_cfg},\n\t{ PCI_VDEVICE(INTEL, PCI_DEVICE_ID_INTEL_IE31200_ADL_S_4), (kernel_ulong_t)&rpl_s_cfg},'
)

with open('/tmp/edac-dkms/ie31200_edac.c', 'w') as f:
    f.write(content)

print("Patched successfully")
