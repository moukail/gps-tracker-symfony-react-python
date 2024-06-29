<?php

namespace App\Model;

use Symfony\Component\Validator\Constraints as Assert;

readonly class LocationDto
{
    public function __construct(
        #[Assert\NotBlank]
        public float $latitude,
        #[Assert\NotBlank]
        public float $longitude,
        #[Assert\NotBlank]
        public float $altitude,
    ) {}
}