<?php

namespace App\Entity;

use App\Repository\LocationRepository;
use DateTime;
use DateTimeInterface;
use Doctrine\ORM\Mapping as ORM;
use Symfony\Component\Serializer\Attribute\Groups;

#[ORM\Entity(repositoryClass: LocationRepository::class)]
#[ORM\HasLifecycleCallbacks]
class Location
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column]
    private ?int $id = null;

    #[ORM\Column]
    #[Groups(["user", "manager"])]
    private float $latitude;

    #[ORM\Column]
    #[Groups(["user", "manager"])]
    private float $longitude;

    #[ORM\Column]
    #[Groups(["user", "manager"])]
    private float $altitude;

    #[ORM\ManyToOne(targetEntity: Device::class)]
    private Device $device;

    #[ORM\Column]
    private DateTime $createdAt;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getLatitude(): string
    {
        return $this->latitude;
    }

    public function setLatitude(string $latitude): Location
    {
        $this->latitude = $latitude;
        return $this;
    }

    public function getLongitude(): string
    {
        return $this->longitude;
    }

    public function setLongitude(string $longitude): Location
    {
        $this->longitude = $longitude;
        return $this;
    }

    public function getAltitude(): string
    {
        return $this->altitude;
    }

    public function setAltitude(string $altitude): Location
    {
        $this->altitude = $altitude;
        return $this;
    }

    public function getDevice(): Device
    {
        return $this->device;
    }

    public function setDevice(Device $device): Location
    {
        $this->device = $device;
        return $this;
    }

    public function getCreatedAt(): DateTimeInterface
    {
        return $this->createdAt;
    }

    #[ORM\PrePersist]
    public function setCreatedAt(): void
    {
        $this->createdAt = new DateTime();
    }
}