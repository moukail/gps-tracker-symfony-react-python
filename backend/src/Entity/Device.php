<?php

namespace App\Entity;

use App\Repository\DeviceRepository;
use DateTime;
use DateTimeInterface;
use Doctrine\ORM\Mapping as ORM;
use Symfony\Bridge\Doctrine\Types\UuidType;
use Symfony\Component\Serializer\Attribute\Groups;
use Symfony\Component\Uid\Uuid;

#[ORM\Entity(repositoryClass: DeviceRepository::class)]
#[ORM\HasLifecycleCallbacks]
class Device
{
    #[ORM\Id]
    #[ORM\Column(type: UuidType::NAME, unique: true)]
    #[ORM\GeneratedValue(strategy: 'CUSTOM')]
    #[ORM\CustomIdGenerator(class: 'doctrine.uuid_generator')]
    #[Groups(["user", "manager"])]
    private ?Uuid $id = null;

    #[ORM\Column(unique: true)]
    #[Groups(["user", "manager"])]
    private ?string $mac = null;

    #[ORM\Column(unique: true)]
    #[Groups(["user", "manager"])]
    private ?string $ipAddress = null;

    #[ORM\Column]
    #[Groups(["user", "manager"])]
    private DateTime $createdAt;

    #[ORM\Column]
    #[Groups(["user", "manager"])]
    private DateTime $updatedAt;

    #[ORM\ManyToOne(targetEntity: User::class)]
    private User $user;

    public function getId(): ?Uuid
    {
        return $this->id;
    }

    public function getMac(): ?string
    {
        return $this->mac;
    }

    public function setMac(?string $mac): Device
    {
        $this->mac = $mac;
        return $this;
    }

    public function getIpAddress(): ?string
    {
        return $this->ipAddress;
    }

    public function setIpAddress(?string $ipAddress): Device
    {
        $this->ipAddress = $ipAddress;
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

    public function getUpdatedAt(): DateTime
    {
        return $this->updatedAt;
    }

    #[ORM\PreUpdate]
    #[ORM\PrePersist]
    public function setUpdatedAt(): void
    {
        $this->updatedAt = new DateTime();
    }

    public function getUser(): User
    {
        return $this->user;
    }

    public function setUser(User $user): Device
    {
        $this->user = $user;
        return $this;
    }
}