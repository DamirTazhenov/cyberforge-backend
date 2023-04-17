from django.db import models



class BaseModel(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        abstract = True


class Cooling(BaseModel):
    TYPE_CHOICES = [
        ('CPU Cooler', 'CPU Cooler'),
        ('Case Fan', 'Case Fan'),
        ('Liquid Cooler', 'Liquid Cooler')
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    socket = models.CharField(max_length=50)
    maximum_noise_level = models.PositiveIntegerField()

    # maximum_tdp = models.PositiveIntegerField()
    # fan_diameter = models.PositiveIntegerField()
    # maximum_rotation_speed = models.PositiveIntegerField()
    # adjustable_speed = models.BooleanField(default=False)
    # cooler_height = models.PositiveIntegerField()
    # connector = models.CharField(max_length=8)
    # air_flow = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return f"{self.type} for {self.socket}"


class Housing(BaseModel):
    CASE_FORM_FACTOR_CHOICES = [
        ('Mini Tower', 'Mini Tower'),
        ('Midi Tower', 'Midi Tower'),
        ('Full Tower', 'Full Tower'),
    ]

    case_form_factor = models.CharField(max_length=10, choices=CASE_FORM_FACTOR_CHOICES)
    compatible_board_form_factor = models.CharField(max_length=10)
    power_supply_unit_location = models.CharField(max_length=10)
    number_of_5_25_bays = models.PositiveIntegerField()
    number_of_3_5_internal_bays = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.case_form_factor} case for {self.compatible_board_form_factor} motherboards"


class PowerSupplyUnit(BaseModel):
    STANDARD_CHOICES = [
        ('80 PLUS', '80 PLUS'),
        ('80 PLUS Bronze', '80 PLUS Bronze'),
        ('80 PLUS Silver', '80 PLUS Silver'),
        ('80 PLUS Gold', '80 PLUS Gold'),
        ('80 PLUS Platinum', '80 PLUS Platinum'),
    ]

    power = models.PositiveIntegerField()
    standard = models.CharField(max_length=16, choices=STANDARD_CHOICES)
    power_connectors = models.CharField(max_length=20)
    pci_e_connectors = models.PositiveIntegerField()
    molex_connectors = models.PositiveIntegerField()
    sata_connectors = models.PositiveIntegerField()
    adjustable_fan_speed = models.BooleanField(default=False)

    def __str__(self):
        return f"Power Supply Unit ({self.power}W)"


class RAM(BaseModel):
    MEMORY_TYPE_CHOICES = [
        ('DDR', 'DDR'),
        ('DDR2', 'DDR2'),
        ('DDR3', 'DDR3'),
        ('DDR4', 'DDR4'),
    ]

    memory_type = models.CharField(max_length=4, choices=MEMORY_TYPE_CHOICES)
    memory_capacity = models.PositiveIntegerField()
    memory_clock_speed = models.PositiveIntegerField()

    # supply_voltage = models.DecimalField(max_digits=3, decimal_places=1)
    # timings = models.CharField(max_length=5)
    # price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.memory_capacity}GB {self.memory_type} RAM ({self.memory_clock_speed}MHz, {self.timings})"


class GraphicsCard(BaseModel):
    CHIPSET_MODEL_CHOICES = [
        ('GTX1050Ti', 'GTX1050Ti'),
        ('GTX1060', 'GTX1060'),
        ('GTX1070', 'GTX1070'),
        ('GTX1080', 'GTX1080'),
        ('RTX2060', 'RTX2060'),
        ('RTX2070', 'RTX2070'),
        ('RTX2080', 'RTX2080'),
        ('RTX3060', 'RTX3060'),
        ('RTX3070', 'RTX3070'),
        ('RTX3080', 'RTX3080'),
    ]

    chipset_model = models.CharField(max_length=10, choices=CHIPSET_MODEL_CHOICES)
    gpu_frequency = models.DecimalField(max_digits=6, decimal_places=0)
    video_memory_frequency = models.DecimalField(max_digits=5, decimal_places=0)
    video_memory_type = models.CharField(max_length=6)
    video_memory_capacity = models.PositiveIntegerField()
    rated_power = models.PositiveIntegerField(help_text='in W')
    connectors = models.CharField(max_length=50)
    video_memory_bus_bit_rate = models.PositiveIntegerField()
    number_of_universal_processors = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.chipset_model} {self.video_memory_capacity}GB ({self.video_memory_type}, {self.video_memory_bus_bit_rate}-bit, {self.number_of_universal_processors} CUDA Cores)"


class Motherboard(BaseModel):
    socket = models.CharField(max_length=50)
    form_factor = models.CharField(max_length=50)
    num_memory_slots = models.IntegerField()
    # num_pci_express_slots_x1 = models.IntegerField()
    # num_pci_express_slots_x16 = models.IntegerField()
    power_connectors = models.IntegerField()

    def __str__(self):
        return self.socket + " " + self.form_factor


class Processor(BaseModel):
    PROCESSOR_TYPE_CHOICES = (
        ('Celeron', 'Celeron'),
        ('Core i3', 'Core i3'),
        ('Core i5', 'Core i5'),
        ('Core i7', 'Core i7'),
        ('Core i9', 'Core i9'),
        ('Pentium', 'Pentium'),
        ('Xeon', 'Xeon'),
    )
    SOCKET_CHOICES = (
        ('LGA1151', 'LGA1151'),
        ('LGA1200', 'LGA1200'),
        ('AM4', 'AM4'),
        ('TR4', 'TR4'),
        ('sTRX4', 'sTRX4'),
    )
    processor_type = models.CharField(max_length=10, choices=PROCESSOR_TYPE_CHOICES)
    socket = models.CharField(max_length=10, choices=SOCKET_CHOICES)
    total_number_of_cores = models.PositiveIntegerField()
    total_number_of_threads = models.PositiveIntegerField()
    clock_frequency = models.FloatField()
    process_technology = models.PositiveIntegerField(help_text='in nm')
    rated_power = models.PositiveIntegerField(help_text='in W')

    # microarchitecture = models.CharField(max_length=10)
    # l3_cache_size = models.PositiveIntegerField(help_text='in MB')
    # integrated_graphics_system = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.processor_type} ({self.socket})"


class Memory(BaseModel):
    interface = models.CharField(max_length=20)
    form_factor = models.CharField(max_length=20)
    disk_capacity = models.IntegerField()
    memory_type = models.CharField(max_length=20)
    read_speed = models.FloatField()
    write_speed = models.FloatField()

    # interface_transfer_rate = models.FloatField()

    def __str__(self):
        return f"{self.disk_capacity} GB {self.memory_type} ({self.interface} {self.interface_transfer_rate} Gbit/s)"


# ACCESSORY


class Mouse(models.Model):
    type = models.CharField(max_length=50, choices=[('Wired', 'Wired'), ('Wireless', 'Wireless')])
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Keyboard(models.Model):
    type = models.CharField(max_length=50, choices=[('Wired', 'Wired'), ('Wireless', 'Wireless')])
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Monitor(models.Model):
    resolution = models.CharField(max_length=50)
    refresh_rate = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Microphone(models.Model):
    name = models.CharField(max_length=255)
    type_choices = (
        ('wired', 'Wired'),
        ('wireless', 'Wireless')
    )
    type = models.CharField(max_length=10, choices=type_choices)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Headset(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Accessory(BaseModel):
    # name = models.CharField(max_length=255)
    # total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE, null=True)
    keybord = models.ForeignKey(Keyboard, on_delete=models.CASCADE, null=True)
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE, null=True)
    microphone = models.ForeignKey(Microphone, on_delete=models.CASCADE, null=True)
    headset = models.ForeignKey(Headset, on_delete=models.CASCADE, null=True)


class Modification(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default='')

    housing = models.ForeignKey(Housing, on_delete=models.CASCADE)
    motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE)
    power_supply = models.ForeignKey(PowerSupplyUnit, on_delete=models.CASCADE)
    processor = models.ForeignKey(Processor, on_delete=models.CASCADE)
    graphics_card = models.ForeignKey(GraphicsCard, on_delete=models.CASCADE)
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE)
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE)
    cooling = models.ForeignKey(Cooling, on_delete=models.CASCADE)

    # accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return f"{self.name} {self.housing} {self.processor} {self.graphics_card} {self.memory}"

