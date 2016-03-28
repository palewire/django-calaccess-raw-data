
# DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=10),
# DocumentCloud(id='2712034-Cal-Format-201', start_page=12),
# DocumentCloud(id='2712032-Cal-Errata-201', start_page=2),
OFFICE_CODE_CHOICES = (
    ("APP", "State Appellate Court Justice"),
    ('ASM', 'State Assembly Person'),
    ("Asm", "State Assembly Person"),
    ("asm", "State Assembly Person"),
    ('ASR', 'Assessor'),
    ('ATT', 'Attorney General'),
    ('BED', 'Board of Education'),
    ('BOE', 'Board of Equalization Member'),
    ('BSU', 'Board of Supervisors'),
    ('CAT', 'City Attorney'),
    ('CCB', 'Community College Board'),
    ('CCM', 'City Council Member'),
    ('CON', 'State Controller'),
    ('COU', 'County Counsel'),
    ('CSU', 'County Supervisor'),
    ("csu", "County Supervisor"),
    ('CTR', 'Local Controller'),
    ('DAT', 'District Attorney'),
    ('GOV', 'Governor'),
    ("gov", "Governor"),
    ('INS', 'Insurance Commissioner'),
    ('LTG', 'Lieutenant Governor'),
    ('MAY', 'Mayor'),
    ('OTH', 'Other'),
    ("oth", "Other"),
    ("OTh", "Other"),
    ('PDR', 'Public Defender'),
    ("PER", "Public Employees Retirement System"),
    ('PLN', 'Planning Commissioner'),
    ('SCJ', 'Superior Court Judge'),
    ('SEN', 'State Senator'),
    ('SHC', 'Sheriff-Coroner'),
    ('SOS', 'Secretary of State'),
    ("SPM", "Supreme Court Justice"),
    ('SUP', 'Superintendent of Public Instruction'),
    ('TRE', 'State Treasurer'),
    ('TRS', 'Local Treasurer'),
    # Other codes observed the database but undocumented
    ("05", "Unknown"),
    ("ASS", "Unknown"),  # assessor? state assembly person?
    ("CIT", "Unknown"),  # "City" Juris_Cd?
    ("CTL", "Unknown"),  # Local Controller? "Controlled Committee (F410)" Item_Cd?
    ("F", "Unknown"),
    ("H", "Unknown"),    # State House?
    ("HOU", "Unknown"),  # State House?
    ("LEG", "Unknown"),  # Legislature? "Legal Defense" Expn_Cd? "Legal" Ind_Class?
    ("OF", "Unknown"),
    ("PAC", "Unknown"),
    ("PRO", "Unknown"),  # "Proponent" Entity_Cd?
    ("REP", "Unknown"),  # State Rep?
    ("ST", "Unknown"),
)

JURIS_CODE_CHOICES = (
    ('', 'Unknown'),
    ('ASM', 'Assembly District'),
    ('BOE', 'Board of Equalization District'),
    ('CIT', 'City'),
    ('CTY', 'County'),
    ('LOC', 'Local'),
    ('OTH', 'Other'),
    ('SEN', 'Senate District'),
    ('STW', 'Statewide'),
    ('FED', 'Unknown'),  # Federal?
    ('JR', 'Unknown'),
)
