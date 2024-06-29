<?php

namespace App\Model;

use Symfony\Component\Validator\Constraints as Assert;

class DeviceDto
{
    public function __construct(
        #[Assert\NotBlank]
        public string $mac,
        #[Assert\NotBlank]
        public string $ip
    ) {}
}